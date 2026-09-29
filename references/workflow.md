# 02  Responsibilities and routing for 14 agents

| Agent | Responsibility | Primary output |
| --- | --- | --- |
| A00 | Orchestrator | brief.json; run_manifest.json |
| A01 | Trend research | trends.csv; candidate_accounts.csv |
| A02 | Market and audience fit | audience_fit.csv |
| A03 | Primary data collection | raw/; posts.csv; request_log.jsonl |
| A04 | Alternative data collection | raw/; actor_runs.jsonl |
| A05 | Outlier detection | outliers.csv; baseline_notes.md |
| A06 | Transcript and video teardown | transcripts/; reference_transfer.csv |
| A07 | Comment research | comments.csv; voice_of_customer.md |
| A08 | Article-to-voiceover adaptation | article_map.md; voiceover_draft.md |
| A09 | Hooks and original scripts | hooks.csv; creative_brief.md; script_draft.md |
| A10 | English editing | final_script.md; edit_notes.md |
| A11 | Storyboard and production handoff | storyboard.csv; production_notes.md |
| A12 | Evidence and delivery QA | qa_report.md |
| A13 | Creative testing and iteration | test_plan.csv; variants/; iteration_log.csv |

Standard route: A00 → A01 → A02 → A03 or A04 → A05 → A06 and A07 → A09 → A10 → A11 → A12 → A13. A13 variants return to A12 before delivery; actual publication and testing require separate authorization. Discovery requests use the shared collection layer first, followed by expanded account-baseline collection, avoiding a circular dependency.

Use A08 when an article is supplied; a reference video can enter teardown directly; a headline-only request invokes only the required hook work. A03/A04 share requests and caches and do not duplicate paid collection by default. One assistant may execute roles sequentially; actual delegation requires a supported environment and authorization for multi-agent work.
