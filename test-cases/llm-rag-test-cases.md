# LLM & RAG Test Cases

This document contains manual QA test cases for evaluating an LLM-powered RAG chatbot.

## TC-001: Answer a question supported by the knowledge base

**Test Scenario:** Verify that the chatbot answers a question using relevant retrieved context.

**User Prompt:**  
What is your return policy?

**Expected Result:**  
- The chatbot retrieves the relevant return policy document.
- The response states that customers can return shoes within 30 days.
- The answer is consistent with the retrieved context.
- The chatbot does not add unsupported information.

**Test Type:** Functional / RAG Groundedness

---

## TC-002: Question not supported by retrieved context

**Test Scenario:** Verify chatbot behavior when the retrieved context does not contain the answer.

**User Prompt:**  
Do you sell boots?

**Expected Result:**  
- The chatbot should not invent product availability.
- It should clearly indicate that the available context does not provide enough information.
- The response should remain relevant to the user's question.

**Test Type:** Hallucination / Groundedness / Edge Case

---

## TC-003: Irrelevant question

**Test Scenario:** Verify chatbot behavior for a question unrelated to the shoe store knowledge base.

**User Prompt:**  
What is the capital of France?

**Expected Result:**  
- The chatbot should recognize that the question is outside the application's supported domain.
- It should not fabricate an answer based on unrelated retrieved documents.
- It should redirect the user to shoe-store-related questions when appropriate.

**Test Type:** Out-of-Scope / Safety
