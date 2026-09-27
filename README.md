# North America Video Creative

**Turn a reference video into an original English hook, script, and shot plan.**

An agent skill for analyzing short videos and creating content for North American audiences. Built for creators, marketers, and small teams working on TikTok, Reels, Shorts, and short-video ads.

[中文说明](README.zh-CN.md) · [Skill instructions](SKILL.md) · [36 hook families](references/hooks.md)

## What it does

- Breaks down the opening frame, hook, narrative beats, product demonstration, pacing, and CTA.
- Separates observable evidence from hypotheses about performance.
- Adapts the structure into original creative for your product and audience.
- Provides 36 hook families and four script formats: story, relatable comedy, education, and process.
- Produces timed narration, shot plans, on-screen text, asset requirements, and test variants.

**Reference → teardown → audience/product fit → hooks → script and shots → variants → measured iteration.**

This is a creative workflow, not a complete GTM system, video renderer, or guarantee of viral reach.

## Install in Codex

Clone this repository into your personal skills directory. If you use a custom `CODEX_HOME`, substitute that directory for `~/.codex`.

```sh
git clone https://github.com/trsgogogo/north-america-video-creative.git ~/.codex/skills/north-america-video-creative
```

Use a new session if the skill is not yet listed. For another agent that supports SKILL.md-based skills, place the repository in that agent's documented skills directory. Automatic discovery depends on the host agent.

## Try it

```text
Use $north-america-video-creative to break down this reference video,
then create an original 30-second English script for my product.

Audience: US independent coffee shop owners
Product: a reusable order-prep checklist
Goal: download the checklist
Reference: [attach video or provide an accessible URL]
```

```text
Give me 10 declarative English hooks for this topic.
Pick the strongest three and expand one into a relatable comedy script.
```

```text
Compare these two video versions using the attached performance data.
Separate observations from hypotheses and propose the next creative test.
```

## What to provide

A video/link/transcript, your product, audience/locale, target duration, channel, desired action, and any real proof or offer terms. A transcript-only analysis cannot establish visual pacing or camera work; the skill makes that limitation explicit.

Default style: benefit-first declarative titles, natural spoken English, concrete scenes, and optional dry humor. Override these preferences in your prompt.

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Entry point and mode selection |
| `references/video-teardown.md` | Evidence-aware video analysis and adaptation |
| `references/hooks.md` | 36 hook families with original examples |
| `references/scripts.md` | Four script formats and production handoff |
| `references/creative-iteration.md` | Creative tests and feedback |
| `references/source-mapping.md` | Methodology and scope |
| `agents/openai.yaml` | Codex display metadata |

## Evidence and limits

No fabricated testimonials, credentials, personal results or scarcity. Examples are illustrative. Viewing metrics alone cannot show that a hook caused success. The skill produces instructions and creative deliverables; media access and rendering depend on tools in the host agent.

## Contributing

Open an issue or pull request with a reproducible example, the expected behavior, and the proposed change. Remove private customer data and use only reference media you can share. Improvements to localization, examples, and evidence-aware analysis are welcome.

## License

[MIT](LICENSE). Third-party reference media and source materials are not included or licensed by this project.
