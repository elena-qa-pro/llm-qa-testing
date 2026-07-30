from deepeval.test_case import LLMTestCase
from deepeval.metrics import ContextualRelevancyMetric, FaithfulnessMetric, AnswerRelevancyMetric


def test_return_policy_context():
    test_case = LLMTestCase(
        input="What is your return policy?",
        actual_output="Customers can return shoes within 30 days for a full refund.",
        retrieval_context=[
            "We offer a 30-day full refund policy at no extra cost for all shoes."
        ]
    )

    metric = ContextualRelevancyMetric(
        threshold=0.7,
        model="gpt-4.1",
        include_reason=True,
        verbose_mode=True
    )

    metric.measure(test_case)
    print("Score:", metric.score)
    print("Reason:", metric.reason)

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
        threshold=0.7,
        model="gpt-4.1"
    )

    metric.measure(test_case)

    assert metric.score < 0.7


def test_hallucinated_return_policy():
    test_case = LLMTestCase(
        input="What is your return policy?",
        actual_output="Customers can return shoes within 60 days for a full refund.",
        retrieval_context=[
            "We offer a 30-day full refund policy at no extra cost for all shoes."
        ]
    )

    metric = FaithfulnessMetric(
        threshold=0.7,
        model="gpt-4.1"
    )

    metric.measure(test_case)

    assert metric.score < 0.7

def test_irrelevant_answer():
    test_case = LLMTestCase(
        input="How long does shipping take?",
        actual_output="Customers can return shoes within 30 days for a full refund."
    )

    metric = AnswerRelevancyMetric(
        threshold=0.7,
        model="gpt-4.1"
    )

    metric.measure(test_case)

    assert metric.score < 0.7
