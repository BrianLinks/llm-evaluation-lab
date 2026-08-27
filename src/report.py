import csv
from pathlib import Path

from src.scoring import classify_quality


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "evaluation_results.csv"


def load_results():
    """Load evaluation results from the CSV dataset."""

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def calculate_metrics(results):
    """Calculate average evaluation metrics across all responses."""

    total = len(results)

    if total == 0:
        raise ValueError("No evaluation results found.")

    metrics = {
        "accuracy": sum(float(row["accuracy"]) for row in results) / total,
        "relevance": sum(float(row["relevance"]) for row in results) / total,
        "completeness": sum(float(row["completeness"]) for row in results) / total,
        "instruction_following": sum(
            float(row["instruction_following"]) for row in results
        ) / total,
    }

    hallucination_count = sum(
        float(row["hallucination"]) > 0 for row in results
    )

    metrics["hallucination_rate"] = (
        hallucination_count / total
    ) * 100

    weighted_score = (
        (metrics["accuracy"] * 0.35)
        + (metrics["relevance"] * 0.25)
        + (metrics["completeness"] * 0.20)
        + (metrics["instruction_following"] * 0.20)
    )

    metrics["overall_score"] = (weighted_score / 5) * 100

    return metrics


def generate_report(metrics, response_count):
    """Generate a human-readable evaluation report."""

    quality = classify_quality(metrics["overall_score"])

    report = f"""
==================================================
              LLM QUALITY REPORT
==================================================

Responses evaluated:       {response_count}

Accuracy:                  {metrics["accuracy"]:.2f} / 5
Relevance:                 {metrics["relevance"]:.2f} / 5
Completeness:              {metrics["completeness"]:.2f} / 5
Instruction Following:     {metrics["instruction_following"]:.2f} / 5

Hallucination Rate:        {metrics["hallucination_rate"]:.2f}%

--------------------------------------------------

Overall Quality Score:     {metrics["overall_score"]:.2f} / 100
Classification:            {quality}

==================================================
"""

    return report


def main():
    """Run the complete evaluation reporting pipeline."""

    results = load_results()

    metrics = calculate_metrics(results)

    report = generate_report(metrics, len(results))

    print(report)


if __name__ == "__main__":
    main()