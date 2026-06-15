# Systek Fagdag 2026 -- LLM Dashboard Demo

[![Fully hand crafted](https://bollaberg.github.io/llm-badges/assets/fully-hand-crafted.svg)](https://bollaberg.github.io/llm-badges/badge-detail.html?id=fully-hand-crafted)

This repository contains a demo of how to create a simple dashboard that uses an LLM (through Google's ADK) to fetch
data from a database and answer user questions in a Streamlit dashboard.

The LLM agent is defined in `fagdag_demo/agent.py`.

## Data

The data for this project is retrieved from the [International-football-results-from-1872-to-2017](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017) project on Kaggle. The data was retrieved on June 12th 2026.

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
streamlit run fagdag_demo/dashboard.py
```


## Presentation

The presentation used for Systek Fagdag 2026 can be found in the `presentation` folder, in either HTML or PDF format.

The presentation is built using [quarto](https://quarto.org/). To render it in preview mode, run:

```bash
quarto preview presentation/fagdag-2026.qmd
```

To compile it without preview mode, run

```bash
quarto render presentation/fagdag-2026.qmd
```

To compile to PDF, do the following steps:
1. Run one of the above commands
2. Open the HTML file at `presentation/fagdag-2026.html`
3. Follow the steps in [Quarto's own documentation](https://quarto.org/docs/presentations/revealjs/presenting.html#print-to-pdf).

> [!NOTE]
> The presentation is in Norwegian

## Archival status

Note that the presentation has been held, so the project is now archived. Feel free to make a fork or copy the project if you want to try it yourself!

