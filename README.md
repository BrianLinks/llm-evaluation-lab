# LLM Evaluation Lab

A practical Python-based framework for evaluating the quality of LLM-generated responses.

I built this project around a simple problem: an AI response can look good at first glance and still fail in important ways. It might answer the wrong part of a question, miss an important instruction, leave out key information, or confidently make something up.

Instead of treating response quality as one number, this project breaks it into measurable areas and combines them into an overall score.

## What This Project Does

The evaluation pipeline looks at five main areas:

- **Accuracy** — Is the information correct?
- **Relevance** — Does the response actually address the user's request?
- **Completeness** — Did it cover the important parts of the task?
- **Instruction Following** — Did it follow the instructions given by the user?
- **Hallucination** — Does the response contain unsupported or fabricated information?

The first four dimensions use a 0–5 scoring scale. They are then combined using weighted scoring to produce a final quality score out of 100.

Hallucination is tracked separately because a response can score well across the other dimensions and still be unreliable if it contains fabricated information.

## Why I Built It

LLM evaluation is easy to make subjective.

Two people can look at the same response and come away with different opinions about whether it was "good." A structured evaluation process makes that judgment easier to reproduce and compare.

For example, imagine an AI assistant is asked:

> "Give me three advantages of remote work and keep the answer under 100 words."

A response could contain three perfectly valid advantages but still fail the evaluation if it ignores the 100-word limit.

That's why I treat **instruction following as its own evaluation dimension**, rather than assuming factual accuracy automatically means the response was good.

## Evaluation Framework

| Dimension | Weight | What I Look For |
|---|---:|---|
| Accuracy | 35% | Factual correctness and reliable information |
| Relevance | 25% | Whether the response stays focused on the request |
| Completeness | 20% | Whether important parts of the task were covered |
| Instruction Following | 20% | Whether explicit requirements were followed |
| Hallucination | Separate | Unsupported or fabricated information |

The weighted score is converted from the 0–5 scale into a score out of 100.

### Quality Classification

| Score | Classification |
|---:|---|
| 90–100 | Excellent |
| 80–89 | Strong |
| 70–79 | Acceptable |
| 60–69 | Needs Improvement |
| Below 60 | Poor |

## Current Sample Results

The current sample dataset produces:

```text
Instruction Following: 4.90 / 5

Hallucination Rate: 0.00%

Overall Quality Score: 96.20 / 100

Classification: Excellent




## Dashboard

The project includes a Streamlit dashboard for viewing the evaluation results without having to inspect CSV files or terminal output manually.

The dashboard currently shows:

- Overall quality score
- Quality classification
- Number of evaluated responses
- Hallucination rate
- Accuracy
- Relevance
- Completeness
- Instruction following
- Evaluation results
- Score distribution
- Evaluation methodology

To start the dashboard locally:

```bash
py -m streamlit run dashboard/app.py
