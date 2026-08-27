from dataclasses import dataclass
from typing import Dict


@dataclass
class EvaluationResult:
    prompt: str
    response: str
    accuracy: float
    relevance: float
    completeness: float
    instruction_following: float
    overall_score: float


class LLMEvaluator:
    """
    Core evaluation engine for assessing AI-generated responses.

    Scores are normalized on a 0-5 scale.
    """

    def __init__(self):
        self.criteria = [
            "accuracy",
            "relevance",
            "completeness",
            "instruction_following",
        ]

    def evaluate(
        self,
        prompt: str,
        response: str,
        scores: Dict[str, float],
    ) -> EvaluationResult:
        """Evaluate an AI response using predefined quality dimensions."""

        self._validate_scores(scores)

        overall_score = sum(scores.values()) / len(scores)

        return EvaluationResult(
            prompt=prompt,
            response=response,
            accuracy=scores["accuracy"],
            relevance=scores["relevance"],
            completeness=scores["completeness"],
            instruction_following=scores["instruction_following"],
            overall_score=round(overall_score, 2),
        )

    def _validate_scores(self, scores: Dict[str, float]) -> None:
        """Validate that all required evaluation scores are present."""

        missing = set(self.criteria) - set(scores.keys())

        if missing:
            raise ValueError(
                f"Missing evaluation criteria: {', '.join(sorted(missing))}"
            )

        for criterion in self.criteria:
            score = scores[criterion]

            if not isinstance(score, (int, float)):
                raise TypeError(
                    f"{criterion} score must be numeric."
                )

            if not 0 <= score <= 5:
                raise ValueError(
                    f"{criterion} score must be between 0 and 5."
                )