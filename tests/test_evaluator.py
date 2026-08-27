import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.evaluator import LLMEvaluator
from src.scoring import calculate_weighted_score, classify_quality


def test_llm_evaluation():
    evaluator = LLMEvaluator()

    result = evaluator.evaluate(
        prompt="Explain artificial intelligence in simple terms.",
        response="Artificial intelligence allows computers to perform tasks that normally require human intelligence.",
        scores={
            "accuracy": 5,
            "relevance": 5,
            "completeness": 4,
            "instruction_following": 5,
        },
    )

    assert result.overall_score == 4.75


def test_weighted_score():
    score = calculate_weighted_score(
        {
            "accuracy": 5,
            "relevance": 4,
            "completeness": 4,
            "instruction_following": 5,
        }
    )

    assert score == 91.0


def test_quality_classification():
    assert classify_quality(95) == "Excellent"
    assert classify_quality(85) == "Strong"
    assert classify_quality(75) == "Acceptable"
    assert classify_quality(65) == "Needs Improvement"
    assert classify_quality(50) == "Poor"