"""Validate local packaging without network access or paid API calls."""
from pathlib import Path
from zipfile import ZipFile
import csv
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []
for file in ROOT.rglob('*'):
    if not file.is_file() or '.git' in file.parts or '__pycache__' in file.parts:
        continue
    if file.suffix == '.docx':
        with ZipFile(file) as archive:
            root = ET.fromstring(archive.read('word/document.xml'))
            text = '\n'.join(t.text or '' for t in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))
    else:
        text = file.read_text(encoding='utf-8')
    if re.search(r'[\u4e00-\u9fff]', text):
        errors.append(f'Non-English CJK text: {file.relative_to(ROOT)}')
    if re.search(r'/(?:Users|home)/[A-Za-z0-9_.-]+/', text):
        errors.append(f'Personal filesystem path: {file.relative_to(ROOT)}')
    if re.search(r'(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |EC |OPENSSH |ENCRYPTED )?PRIVATE KEY-----', text):
        errors.append(f'Possible credential: {file.relative_to(ROOT)}')
    if file.suffix == '.md':
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if target.startswith(('https://', 'http://', '#', 'mailto:')):
                continue
            local = target.split('#')[0]
            if local and not (file.parent / local).exists():
                errors.append(f'Broken link: {file.relative_to(ROOT)} -> {target}')
    if file.suffix == '.csv':
        with file.open(newline='') as handle:
            fields = next(csv.reader(handle))
        if len(set(fields)) != len(fields) or any(not value for value in fields):
            errors.append(f'Invalid CSV header: {file.name}')
for index in range(14):
    matches = list((ROOT / 'prompts').glob(f'A{index:02}-*.md'))
    if len(matches) != 1 or '```text' not in matches[0].read_text():
        errors.append(f'Missing full prompt A{index:02}')
hooks = (ROOT / 'references/hooks.md').read_text()
if len(re.findall(r'^## \d{2} ', hooks, re.M)) != 36:
    errors.append('Expected 36 numbered hook families')
skill = (ROOT / 'SKILL.md').read_text()
if not skill.startswith('---\nname: short-form-content-os\ndescription:'):
    errors.append('Missing skill metadata')
if errors:
    raise SystemExit('\n'.join(errors))
print('PASS: 14 complete role prompts, 36 hook families, local links, English text, CSV headers and public-file checks.')
print('No API collection, media rendering or paid tests executed.')
