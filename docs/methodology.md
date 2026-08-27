# Evaluation Methodology

## Overview

LLM Evaluation Lab uses a structured scoring system to measure the quality of AI-generated responses.

Each response is evaluated across four quality dimensions:

- Accuracy
- Relevance
- Completeness
- Instruction Following

Hallucination is tracked separately as a reliability metric.

## Evaluation Dimensions

### Accuracy

Measures whether the information in the response is factually correct.

### Relevance

Measures whether the response directly addresses the user's request without unnecessary off-topic information.

### Completeness

Measures whether the response covers the important parts of the task.

### Instruction Following

Measures whether the response follows the explicit requirements in the prompt, such as format, length, structure, or required information.

Each dimension is scored from **0 to 5**.

## Weighted Scoring

The four dimensions use the following weights:

| Dimension | Weight |
|---|---:|
| Accuracy | 35% |
| Relevance | 25% |
| Completeness | 20% |
| Instruction Following | 20% |

The weighted score is calculated using:

```text
(Accuracy × 0.35)
+ (Relevance × 0.25)
+ (Completeness × 0.20)
+ (Instruction Following × 0.20)