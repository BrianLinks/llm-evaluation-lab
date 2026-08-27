# LLM Evaluation Lab

A practical Python-based framework for evaluating the quality of LLM-generated responses using structured, measurable criteria.

I built this project around a simple problem: an AI response can look good at first glance and still fail in important ways. It might answer the wrong part of a question, miss an important instruction, leave out key information, or confidently make something up.

Instead of treating response quality as one number, this project breaks it into measurable areas and combines them into an overall quality score.

## What This Project Does

The evaluation pipeline measures four core quality dimensions:

* **Accuracy** — Is the information correct?
* **Relevance** — Does the response actually address the user's request?
* **Completeness** — Did it cover the important parts of the task?
* **Instruction Following** — Did it follow the instructions given by the user?

Hallucination is tracked separately as a reliability metric.

The four core dimensions use a 0–5 scoring scale and are combined using weighted scoring to produce a final quality score out of 100.

## Why I Built It

LLM evaluation can easily become subjective.

Two people can look at the same response and come away with different opinions about whether it was "good." A structured evaluation process makes that judgment easier to reproduce, compare, and analyze.

For example, imagine an AI assistant is asked:

> "Give me three advantages of remote work and keep the answer under 100 words."

A response could contain three perfectly valid advantages but still fail the evaluation if it ignores the 100-word limit.

That's why **Instruction Following** is treated as its own evaluation dimension rather than assuming that factual accuracy automatically means the response was successful.

## Evaluation Framework

| Dimension             |   Weight | What I Look For                                   |
| --------------------- | -------: | ------------------------------------------------- |
| Accuracy              |      35% | Factual correctness and reliable information      |
| Relevance             |      25% | Whether the response stays focused on the request |
| Completeness          |      20% | Whether important parts of the task were covered  |
| Instruction Following |      20% | Whether explicit requirements were followed       |
| Hallucination         | Separate | Unsupported or fabricated information             |

Each of the four core dimensions is scored from **0 to 5**.

The weighted score is calculated as:

```text
(Accuracy × 0.35)
+ (Relevance × 0.25)
+ (Completeness × 0.20)
+ (Instruction Following × 0.20)
```

The result is then normalized to a 0–100 scale:

```text
Overall Score = (Weighted Score / 5) × 100
```

## Quality Classification

|    Score | Classification    |
| -------: | ----------------- |
|   90–100 | Excellent         |
| 80–89.99 | Strong            |
| 70–79.99 | Acceptable        |
| 60–69.99 | Needs Improvement |
| Below 60 | Poor              |

## Hallucination Rate

Hallucination is measured separately from the weighted quality score.

A response is counted as containing hallucination when its hallucination value is greater than zero.

```text
Hallucination Rate =
(Hallucinated Responses / Total Responses) × 100
```

Keeping hallucination separate provides an additional reliability signal. A response can perform well across the four quality dimensions while still requiring attention if unsupported or fabricated information is detected.

## Current Sample Results

The current sample dataset contains **10 evaluated responses**.

```text
Accuracy:                  4.80 / 5
Relevance:                 5.00 / 5
Completeness:              4.50 / 5
Instruction Following:     4.90 / 5

Hallucination Rate:        0.00%

Overall Quality Score:     96.20 / 100
Classification:            Excellent
```

These results represent the current sample dataset and are not intended to represent the performance of a production model.

## Dashboard

The project includes a Streamlit dashboard for viewing evaluation results without having to inspect CSV files or terminal output manually.

The dashboard currently provides:

* Overall quality score
* Quality classification
* Number of evaluated responses
* Hallucination rate
* Accuracy
* Relevance
* Completeness
* Instruction Following
* Evaluation results
* Score distribution
* Evaluation methodology

### Run the Dashboard

From the project root:

```bash
py -m streamlit run dashboard/app.py
```

## Project Structure

```text
llm-evaluation-lab/
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── evaluation_results.csv
│
├── docs/
│   └── methodology.md
│
├── src/
│   ├── evaluator.py
│   ├── scoring.py
│   └── report.py
│
├── tests/
│   └── test_evaluator.py
│
├── .gitignore
├── LICENSE
└── README.md
```

## Core Components

### `src/evaluator.py`

Provides the core evaluation interface.

It:

* Validates evaluation scores
* Ensures required criteria are present
* Ensures scores are numeric
* Ensures scores fall between 0 and 5
* Produces a structured `EvaluationResult`
* Uses the centralized weighted scoring function

### `src/scoring.py`

Contains the project's scoring logic.

It defines:

* Evaluation weights
* Weighted score calculation
* Quality classification thresholds

This module acts as the central source of truth for the project's weighted scoring methodology.

### `src/report.py`

Provides the dataset-level reporting pipeline.

It:

* Loads evaluation results from CSV
* Calculates average evaluation metrics
* Calculates hallucination rate
* Calculates the weighted overall quality score
* Assigns a quality classification
* Generates a human-readable report

### `dashboard/app.py`

Provides an interactive Streamlit interface for exploring the evaluation dataset and results.

### `tests/test_evaluator.py`

Contains automated tests covering:

* Core evaluator behavior
* Weighted score calculation
* Quality classification

Run the tests with:

```bash
py -m pytest
```

Current test result:

```text
3 passed
```

## Methodology

A detailed explanation of the scoring methodology is available in:

```text
docs/methodology.md
```

The methodology documents the evaluation dimensions, scoring weights, normalization process, quality classifications, hallucination calculation, dataset-level evaluation, and current limitations.

## Example Evaluation

A response can be evaluated using the core evaluator:

```python
from src.evaluator import LLMEvaluator

evaluator = LLMEvaluator()

result = evaluator.evaluate(
    prompt="Explain artificial intelligence in simple terms.",
    response=(
        "Artificial intelligence allows computers to perform "
        "tasks that normally require human intelligence."
    ),
    scores={
        "accuracy": 5,
        "relevance": 5,
        "completeness": 4,
        "instruction_following": 5,
    },
)

print(result.overall_score)
```

The evaluator uses the same weighted scoring methodology as the reporting pipeline.

## Design Principles

The project is built around a few simple principles:

**Measurable:**
Response quality is separated into clearly defined evaluation dimensions.

**Consistent:**
Scores use a standardized 0–5 scale and predefined weights.

**Transparent:**
The scoring formula and classification thresholds are documented and implemented directly in Python.

**Reproducible:**
Evaluation results can be stored in a structured dataset and processed using the same reporting pipeline.

**Extensible:**
The framework is intentionally lightweight so additional evaluation dimensions, datasets, automated judges, and benchmarking capabilities can be added later.

## Limitations

The current implementation is intentionally lightweight.

The evaluation dataset uses predefined evaluation scores rather than automatically generating judgments with another language model. As a result, the quality of the final analysis depends on the consistency of the underlying evaluation judgments.

The current framework also does not yet include:

* Automated fact verification
* Automated hallucination detection
* Model-to-model benchmarking
* Inter-rater agreement analysis
* Confidence intervals
* Large-scale evaluation datasets

## Future Improvements

Potential future improvements include:

* Adding multiple human evaluators
* Measuring inter-rater agreement
* Adding LLM-as-a-judge evaluation
* Automated factual verification
* Automated hallucination detection
* Confidence scoring
* Larger and more diverse evaluation datasets
* Multilingual evaluation
* Model-to-model comparison
* Historical evaluation tracking

## Technologies

* **Python**
* **Pandas**
* **Streamlit**
* **Pytest**
* **CSV**
* **Git / GitHub**

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
