from typing import Dict


WEIGHTS = {
    "accuracy": 0.35,
    "relevance": 0.25,
    "completeness": 0.20,
    "instruction_following": 0.20,
}


def calculate_weighted_score(scores: Dict[str, float]) -> float:
    """
    Calculate a weighted AI response quality score.

    Each criterion is scored from 0-5.
    The final score is returned on a 0-100 scale.
    """

    missing = set(WEIGHTS) - set(scores)

    if missing:
        raise ValueError(
            f"Missing scoring criteria: {', '.join(sorted(missing))}"
        )

    weighted_score = sum(
        scores[criterion] * weight
        for criterion, weight in WEIGHTS.items()
    )

    return round((weighted_score / 5) * 100, 2)


def classify_quality(score: float) -> str:
    """Convert a numerical score into a quality category."""

    if score >= 90:
        return "Excellent"
    if score >= 80:
        return "Strong"
    if score >= 70:
        return "Acceptable"
    if score >= 60:
        return "Needs Improvement"

    return "Poor"