# Research integrations

The workflow is usable with supplied links, transcripts, articles and metrics. Automated collection needs separately installed providers and credentials; this repository does not include an API backend or bundled credits.

| Skill | Job | Upstream |
| --- | --- | --- |
| outlier-post-finder | Compare posts with their account baseline | [ScrapeCreators skills](https://github.com/ScrapeCreators/social-media-research-skills) |
| trend-discovery | Discover topics, sounds, formats and examples | [ScrapeCreators skills](https://github.com/ScrapeCreators/social-media-research-skills) |
| transcript-intelligence | Analyze actual transcripts | [ScrapeCreators skills](https://github.com/ScrapeCreators/social-media-research-skills) |
| comment-mining | Extract questions, objections and needs | [ScrapeCreators skills](https://github.com/ScrapeCreators/social-media-research-skills) |
| audience-research | Assess market fit from available evidence | [ScrapeCreators skills](https://github.com/ScrapeCreators/social-media-research-skills) |
| scrapecreators-api | Primary collection provider | [ScrapeCreators skills](https://github.com/ScrapeCreators/social-media-research-skills) |
| apify-ultimate-scraper | Alternative collection provider | [Apify agent skills](https://github.com/apify/agent-skills) |

Follow each upstream project's current installation and license instructions. Only install the tools needed by your task. The original third-party SKILL.md files are not vendored or relicensed here.

ScrapeCreators requests use `SCRAPECREATORS_API_KEY`; Apify uses an existing login or `APIFY_TOKEN`. Keep credentials in your host environment, never in prompts or tracked files. Set an explicit collection/result cap and cost budget. Check current endpoints, Actor inputs, pagination, supported filters and pricing at execution time.

Start with a small pilot when using an unfamiliar collection route. A result cap is not always a billing cap. Use the same cache across both providers. If services are unavailable, report a plan and missing configuration rather than invented results.

No paid API calls or platform collection were performed to validate this repository release. Local validation covers content structure, packaging and links.
