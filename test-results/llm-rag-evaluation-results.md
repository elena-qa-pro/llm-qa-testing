# LLM & RAG Evaluation Results

This document records manual QA evaluation results for an LLM-powered RAG chatbot.

## Test Execution Summary

- Application: Shoe Store RAG Chatbot
- Test Method: Manual LLM/RAG evaluation
- Areas Tested: Groundedness, relevance, hallucination, retrieval quality, and edge cases

---

## TC-001: Supported Question

**User Prompt:**  
What is your return policy?

**Retrieved Context:**  
The knowledge base states that customers can return shoes within 30 days for a full refund.

**Observed Response:**  
The chatbot stated that customers can return shoes within 30 days and provided a full refund policy.

**Evaluation:**
- Groundedness: PASS
- Relevance: PASS
- Retrieval Quality: PASS
- Hallucination: PASS

**Overall Result:** PASS

**Notes:**  
The response was consistent with the retrieved context and did not introduce unsupported information.

---

## TC-002: Answer Not Supported by Retrieved Context

**User Prompt:**  
Do you sell boots?

**Retrieved Context:**  
The retrieved document described professional shoe fitting services but did not contain information about whether boots are sold.

**Observed Response:**  
The chatbot acknowledged that the available context did not specify whether boots were sold and avoided claiming that boots were available.

**Evaluation:**
- Groundedness: PASS
- Relevance: PASS
- Retrieval Quality: FAIL
- Hallucination: PASS

**Overall Result:** PASS WITH OBSERVATION

**Notes:**  
The model handled missing information correctly, but the retrieval did not provide context capable of answering the question.

---

## TC-003: Out-of-Domain Question

**User Prompt:**  
What is the capital of France?

**Expected Behavior:**  
The chatbot should recognize that the question is outside the shoe store knowledge domain and should not fabricate an answer from retrieved store documents.

**Evaluation Criteria:**
- Detect out-of-domain request
- Avoid unsupported RAG-based claims
- Respond appropriately when the knowledge base cannot support the request

**Overall Result:** NOT EXECUTED

**Notes:**  
This scenario is documented for future execution and evaluation.
