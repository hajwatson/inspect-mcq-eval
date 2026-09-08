# MCQ Prompt-Robustness Eval

An evaluation project using the AISI Inspect framework to measure how
multiple-choice benchmark accuracy shifts under trivial reformatting
(e.g. answer-order shuffling).

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your API key
```

## Running

```bash
inspect eval robustness_eval.py@mcq_baseline --model openai/gpt-4o-mini
inspect eval robustness_eval.py@mcq_shuffled --model openai/gpt-4o-mini
```

## Viewing results

```bash
inspect view
```
