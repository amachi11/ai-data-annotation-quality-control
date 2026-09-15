# Annotation Examples & Edge Cases

## Straightforward Example

**Text:** "I was charged twice for the same subscription."

- Category: `BILLING`
- Sentiment: `NEGATIVE`
- Urgency: `MEDIUM`
- Requires Review: `FALSE`

**Reasoning:** The primary issue is an incorrect charge. The customer is reporting a problem but gives no immediate deadline.

---

## Sarcasm

**Text:** "Great, another package that arrived late."

- Category: `DELIVERY`
- Sentiment: `NEGATIVE`
- Urgency: `LOW`
- Requires Review: `TRUE`

**Reasoning:** The word "Great" appears positive in isolation, but the complete sentence is sarcastic and expresses dissatisfaction. The record is flagged so the interpretation is auditable.

---

## Mixed Sentiment

**Text:** "The delivery was late, but your support agent was incredibly helpful."

- Category: `DELIVERY`
- Sentiment: `MIXED`
- Urgency: `LOW`
- Requires Review: `FALSE`

**Reasoning:** The message contains both a negative delivery experience and meaningful positive feedback.

---

## High Urgency

**Text:** "I need access to my account today because I have a deadline tonight."

- Category: `ACCOUNT`
- Sentiment: `NEGATIVE`
- Urgency: `HIGH`
- Requires Review: `FALSE`

**Reasoning:** The customer states a concrete same-day deadline. Urgency is based on impact and timing rather than emotional tone.

---

## Annotation Principle

When evidence is insufficient, the annotator should flag the record for review instead of inventing context. Consistency and traceability are more valuable to an AI training dataset than forced certainty.
