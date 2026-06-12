# Systek Fagdag 2026 -- LLM Dashboard Demo

[![Fully hand crafted](https://bollaberg.github.io/llm-badges/assets/fully-hand-crafted.svg)](https://bollaberg.github.io/llm-badges/badge-detail.html?id=fully-hand-crafted)

This repository contains a demo of how to create a simple dashboard that uses an LLM (through Google's ADK) to fetch
data from a database and answer user questions.

The LLM agent is defined in `fagdag_demo/agent.py`.

## Setup

Setup environment variables by copying `.env.example` to `.env` and filling in the required values.

```bash
cp .env.example .env
```

Install dependencies:

```bash
uv venv
source .venv/bin/activate
uv sync
```

Run the application:

```bash
adk run fagdag_demo
# OR
adk web --port 8000
```

## Presentation

The presentation used for Systek Fagdag 2026 can be found in the `presentation` folder. It is built using [quarto](https://quarto.org/) and can be rendered by running:

```bash
quarto preview presentation/fagdag-2026.qmd
```

Note that the presentation is in Norwegian.
