# 08  Data standards, acceptance and runtime requirements

Use platform+post_id as the key; if absent, use a normalized URL and document it. Use ISO 8601 with explicit timezone and window boundaries.

Preserve platform metric definitions; missing is null, not zero. Do not silently conflate views, plays, shares or saves.

Use same-account/platform/format medians excluding the target. Fewer than ten posts means low confidence; 20+ still requires completeness and age checks.

Growth requires at least two comparable snapshots; lifetime views/age is not recent growth. Record negative deltas as anomalies.

State engagement denominators and included metrics; visible engagement without shares is not total engagement. Comment frequencies need denominators and overlap notes.

Source IDs map to URL/raw file/endpoint/time; claim IDs map speech to source, verified/source_claim/hypothesis/unsupported status and limitations.

Separate creator location, proxy region, content-market signals and audience geography. English proves neither nationality nor audience share.

Version drafts, final copy, storyboards and variants. Storyboard speech must match the final-copy version. Share budget and cache across paid requests.

Use Pass / Fix / Unknown. Repair false facts, invented metrics and critical timing problems before delivery; do not hide them behind an aggregate score.

ScrapeCreators requires SCRAPECREATORS_API_KEY; Apify needs login/APIFY_TOKEN and its CLI. Check the current runtime before execution and never place secrets in artifacts or chat.

Configuration references: https://docs.scrapecreators.com/ ; https://docs.apify.com/ ; https://console.apify.com/settings/integrations . This handbook is not a live audit of endpoint availability, pricing or platform policy.

```text
[output_dir]/[run_id]/
brief.json; run_manifest.json
raw/; logs/request_log.jsonl; logs/actor_runs.jsonl
research/trends.csv; candidate_accounts.csv; audience_fit.csv
research/posts.csv; outliers.csv; baseline_notes.md
research/transcripts/; hook_patterns.md; comments.csv; voice_of_customer.md
creative/reference_transfer.csv; benefit_evidence.csv; creative_brief.md; hooks.csv
evidence/claim_map.csv
scripts/article_map.md; titles.md; script_draft.md; writing_rationale.md
scripts/final_script.md; edit_notes.md
production/storyboard.csv; production_notes.md
testing/test_plan.csv; variants/; iteration_log.csv
qa/qa_report.md
```
