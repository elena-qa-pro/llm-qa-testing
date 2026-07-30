# LLM QA Testing Portfolio
![LLM QA Tests](https://github.com/elena-qa-pro/llm-qa-testing/actions/workflows/main.yml/badge.svg)

QA portfolio project focused on testing LLM and RAG-based applications.

The project demonstrates manual and automated evaluation of AI responses, with focus on:

- Contextual relevancy
- Groundedness
- Hallucination detection
- Retrieval quality
- Edge cases
- Out-of-domain questions
- LLM-as-a-judge evaluation
- CI execution with GitHub Actions

## Project Structure

```text
test-cases/
  llm-rag-test-cases.md
  llm-evaluation-checklist.md

test-results/
  rag-evaluation-results.md

tests/
  test_rag_evaluation.py

.github/workflows/
  main.yml
```

## Automated Evaluation

Automated tests are implemented with:

- Python
- pytest
- DeepEval
- OpenAI evaluation model
- GitHub Actions

The automated test flow is:

**User Prompt → Retrieved Context → LLM Response → DeepEval Metric → PASS / FAIL**

## Current Automated Tests

### Return Policy - Relevant Context

Verifies that relevant return-policy context receives a contextual relevancy score above the configured threshold.

### Irrelevant Context

Verifies that unrelated retrieved context is identified as low relevance.

## CI

GitHub Actions runs the automated RAG evaluation tests in a Python environment.

The workflow installs dependencies and executes:

```bash
pytest tests/test_rag_evaluation.py -v
```

OpenAI credentials are stored securely using GitHub Repository Secrets.

## QA Approach

The project includes both manual and automated AI testing.

Manual evaluation covers:

- Groundedness
- Relevance
- Hallucination
- Retrieval quality
- Edge cases
- Safety and prompt injection

Automated evaluation currently focuses on contextual relevancy using DeepEval.

## Key Learning

LLM testing differs from traditional deterministic testing because a response can be fluent while still being incorrect or unsupported.

For RAG applications, QA should evaluate both:

1. **Retrieval quality** — whether the correct context was retrieved.
2. **Generation quality** — whether the response is grounded in that context.

This project demonstrates both areas through documented test cases, evaluation results, and automated checks.
