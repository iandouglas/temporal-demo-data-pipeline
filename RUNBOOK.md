# Data Pipeline Runbook

These updates are only for AWS re:Invent 2026. Do not merge this branch into the default branch. Contact Ian Douglas or Tomas Josovsky with questions.

[Setup and Walkthrough](#setup-and-walkthrough) | [Booth Setup](#reinvent-2026-booth-setup) | [README](README.md)

## Setup and Walkthrough

Install with `uv sync`. Run `uv run python worker.py` and `uv run python ui/app.py` from the repo root in separate terminals, alongside `temporal server start-dev`. The upstream UI defaults to localhost:8080. For Cloud API keys, set `TEMPORAL_HOST_URL`, `TEMPORAL_NAMESPACE` and `TEMPORAL_API_KEY` in both processes. The booth branch adds API-key support; upstream originally uses mTLS. Add `Step` (Keyword) for AdvancedVisibility. Start with HappyPath, then exercise the signal/update scenarios. Verify each result and Activity retry in Temporal UI. Stop with Ctrl-C; keep `demodata/` intact.

## Sources

[Source README](README.md), [Temporal CLI](https://docs.temporal.io/cli).

## re:Invent 2026 Booth Setup

These updates are only for AWS re:Invent 2026. Do not merge this branch into the default branch. Contact Ian Douglas or Tomas Josovsky with questions.

The laptop bundle uses this demo's source instructions with a separate UI port and a laptop-specific task queue. From the parent `new-demos/` folder, run `./bundle-setup.sh --only data-pipeline` and `python3 bundle.py panel`, then start **Data Pipeline** in [Config](http://127.0.0.1:5199/config). UI: [localhost:5330](http://127.0.0.1:5330/).

Use the shared `.env` from 1Password at the bundle root. Keep machine identity in `.env.local`. The panel keeps local Temporal running in Cloud mode and restarts this demo's owned processes when switching targets. See the [bundle runbook](../RUNBOOK.md) for Cloud prerequisites, offline limits and verification. Runtime is not verified by installation alone.
