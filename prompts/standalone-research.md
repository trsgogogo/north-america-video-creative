# Appendix A  Standalone research prompts

Copy these prompts for standalone research tasks. For the integrated workflow, use the brief quantities, budget and defaults in Chapter 03 of the handbook.

## A1  outlier-post-finder

```text
Use outlier-post-finder to find short-video outliers relevant to North America.
Niche: [AI tools / entrepreneurship / automation / your niche]. Markets: US and Canada, primarily English. Platforms: TikTok, Instagram Reels, YouTube Shorts. Accounts: [handles/profile URLs; otherwise discover relevant accounts and explain selection].
1. Prioritize posts from the last seven days; establish each account's baseline from comparable short videos in the last 30 days.
2. Collect at least 20 comparable posts per account where available. Flag insufficient samples rather than silently widening dates.
3. Calculate median views separately by platform, account and format.
4. Compute lift = video views / account-sample median. Prioritize ≥5x; do not calculate with zero/missing baselines.
5. Consider publication age; do not directly compare fresh posts with long-accumulating ones.
6. Fetch available transcripts for leading videos; analyze hooks, promise, narrative, evidence and CTA.
7. Separate observations from hypotheses; correlation is not causation.
Deliver up to 20 rows: platform, account, source URL, publication/capture time, views, likes, comments, available shares, baseline size/median, lift, North American relevance, hook and reusable format. Propose five original English topics with reference links. Explain in the user's language; preserve English hook quotations. Leave unavailable data blank and explain; never invent speech or shots without access.
```

## A2  trend-discovery

```text
Use trend-discovery to find recent trends for North American short-video creation.
Niche: [category]. Audience: [e.g. US business owners, developers, solo founders]. Markets: US and Canadian English. Platforms: TikTok, Reels, Shorts. Window: the last seven days relative to execution.
Research topics/angles, hashtags/keywords, verifiable trending sounds/music, formats adopted by independent creators, and fit with my audience. Filter irrelevant popularity.
Seek three different-account examples per trend and retain publication/capture times. Reduce confidence when evidence is thin. Separate high current popularity, growth supported by time series and inferred momentum. Without snapshots do not claim weekly growth; English does not prove North American audience.
Output trend, type, evidence links, available metrics, window, market support, audience fit, saturation judgment/reasons and confidence. End with ten English ideas, each containing one hook, a 15–45-second outline, suitable platform and references.
```

## A3  transcript-intelligence

```text
Use transcript-intelligence to analyze these videos: [URLs]. My niche: [niche]. Target audience: [North American segment].
Retrieve actual transcripts first. For each video identify: first sentence/timestamp and first-three-second hook only when timing is reliable; attention mechanism; promised problem solved; problem/context/method/demo/evidence/result/CTA structure; main claims, turning points, examples and checkable facts; lines encouraging continued viewing or explaining product value; requested action.
Separate quotations, explanation and inference. Mark unclear automatic transcription; if unavailable, explicitly limit analysis to accessible titles/descriptions. Text alone does not reveal shots, editing, facial expression or effects.
Deliver per-video breakdowns and recurring structures. Write three original English scripts for my niche: benefit-led, story-led and demonstration-led. Each should fit about 30–45 seconds and include hook, body and CTA. Adapt structure, not distinctive wording; never invent revenue, results or customer cases.
```

## A4  comment-mining

```text
Use comment-mining on these public videos/accounts: [URLs]. Product/niche: [fill]. Market: US and Canadian English.
Start with at most 100 top-level comments per video; count useful replies separately. Record collection method, sorting, time and actual sample.
Group concrete problems, buying objections, recurring questions, requested future content, unmet product needs, explicit price/link/trial interest, and distrust/confusion. Remove obvious duplicates/irrelevance; flag suspected bots/ads without asserting identity.
Give theme counts and denominators with short original English quotations and source links. If no comment permalink exists, provide video URL and locating information. Do not generalize commenters to all viewers, equate inquiries with purchases or infer nationality from English.
Deliver a pain/objection table, ten English topics, five FAQ responses and three product/service opportunities requiring validation. Every recommendation must link to comment evidence.
```

## A5  audience-research

```text
Use audience-research to evaluate these creators/brands: [profile URLs]. Product: [fill]. Buyer: [industry, role, needs, budget]. Regions: [US / Canada / both]. Languages: [English; add French/Spanish when needed].
Check public profile/location/topics; recent language, settings, products, currencies and market context; comment needs relevant to our buyer; audience-region data only where actually available, with definition/source/time; and irrelevant content, unusual interactions or market mismatch signals.
Separate verified audience data, creator self-description and inference from content/comments. Creator residence is not audience geography. Do not invent income, age, gender or country percentages.
For each account provide URL, positioning, location evidence, needs fit, partnership fit, sources, gaps and confidence. Classify prioritize / needs more evidence / deprioritize and explain. Do not contact accounts.
```

## A6  scrapecreators-api

```text
Use scrapecreators-api to collect public short-video research data.
Platform: [TikTok / Reels / Shorts]. Input: [accounts, videos or keywords]. Window: [dates]. Total-result cap: [e.g.100]. Data: [videos / profiles / comments / transcripts].
Verify current endpoints, parameters, pagination, charges and limits before execution. Use environment SCRAPECREATORS_API_KEY without exposing it. If missing, explain the configuration gap and provide an executable request plan; do not fabricate results.
Handle pagination, deduplication, rate limits and bounded retries. Apply date/region filters only when supported and explain limitations. Preserve raw JSON and export normalized CSV. Missing fields are null/blank, not zero. Record request scope, capture time, actual count and incomplete coverage.
Where available include platform, post_id, url, creator_handle, published_at, collected_at, caption, duration_seconds, views, likes, comments, shares, saves, transcript, region_evidence and source_endpoint. Include only returned or supported fields. Deliver file links, a data dictionary and completeness report.
```

## A7  apify-ultimate-scraper

```text
Use apify-ultimate-scraper for North American short-video research.
Niche: [fill]. Platforms: TikTok, Reels, Shorts. Input: [accounts/videos/keywords/hashtags]. Dates: [fill]. Per-platform result cap: [e.g.50]. Output: raw JSON plus normalized CSV.
Evaluate current Actors; candidates include clockworks/tiktok-scraper, apify/instagram-reel-scraper and streamers/youtube-shorts-scraper. Read current input schemas, documentation and pricing; verify supported inputs, dates and regional options rather than assuming stability.
Use existing login/APIFY_TOKEN without revealing secrets. Pilot at most five results per platform, check fields/relevance/actual cost, then expand within the supplied budget. Total budget: [amount; if unset, estimate and plan only, no paid tasks].
Record Actor, run and dataset IDs, time and count; preserve source URLs/raw metrics; deduplicate and export unified CSV plus raw JSON. Proxy/search regions are collection settings, not audience proof. List unsupported filters, missing fields and failed platforms. Do not add platforms or exceed result/cost limits. Deliver summary, file links and supported/unsupported outlier conclusions.
```

## A8  Previous master prompt

```text
Combine the installed short-video research Skills to build a North American reference library.
Niche: [fill]. Audience: [fill]. Accounts: [optional]. Markets: US/Canadian English. Platforms: TikTok, Reels, Shorts. Discovery: seven days. Baseline: 30 days. Total collection cap: [fill]. Budget: [fill].
1. trend-discovery finds trends and candidates.
2. audience-research screens market fit and explains location evidence.
3. scrapecreators-api or apify-ultimate-scraper uses the configured, suitable source without duplicate paid collection.
4. outlier-post-finder creates account/platform baselines and prioritizes ≥5x posts.
5. transcript-intelligence analyzes actual transcripts for the top ten.
6. comment-mining studies their public comments for needs and ideas.
Deliver a CSV with URLs, dates, metrics, baselines, lift and market support; ten video hook/structure analyses; evidence-backed audience needs; ten original English topics and three full English scripts; gaps, collection scope and cost notes.
Explain in the user's language; hooks/scripts in English. Never invent unavailable data, claim outperformance without a baseline, fastest growth without snapshots or audience proportions without data. If services/budget are unavailable, complete independent preparation and list the configuration needed next.
```
