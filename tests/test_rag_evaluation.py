from deepeval.test_case import LLMTestCase
from deepeval.metrics import ContextualRelevancyMetric


def test_return_policy_context():
    test_case = LLMTestCase(
        input="What is your return policy?",
        actual_output="Customers can return shoes within 30 days for a full refund.",
        retrieval_context=[
            "We offer a 30-day full refund policy at no extra cost for all shoes."
        ]
    )

    metric = ContextualRelevancyMetric(
        threshold=0.7
    )

    metric.measure(test_case)

    assert metric.score >= 0.7



def test_irrelevant_context():
    test_case = LLMTestCase(
        input="What is your return policy?",
        actual_output="Customers can return shoes within 30 days for a full refund.",
        retrieval_context=[
            "Our store offers professional shoe fitting services."
        ]
    )

    metric = ContextualRelevancyMetric(
        threshold=0.7
    )

    metric.measure(test_case)

    assert metric.score < 0.7
