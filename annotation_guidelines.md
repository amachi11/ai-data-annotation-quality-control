# Annotation Guidelines

## Purpose

These guidelines define how customer-support text should be labeled for a supervised machine-learning dataset. The goal is to produce labels that are accurate, consistent, reproducible, and easy to audit.

## 1. Category

Choose exactly one primary category.

- `DELIVERY` — shipping, tracking, delays, missing packages, delivery dates
- `BILLING` — charges, payments, refunds, invoices, subscriptions
- `ACCOUNT` — login, password, profile, verification, account access
- `PRODUCT` — product quality, defects, features, availability, performance
- `OTHER` — messages that do not fit the categories above

When a message contains multiple issues, label the issue that is the main reason the customer is contacting support. Flag `requires_review=TRUE` when no primary issue can be determined confidently.

## 2. Sentiment

- `POSITIVE` — clear satisfaction, praise, or appreciation
- `NEGATIVE` — dissatisfaction, frustration, complaint, or disappointment
- `NEUTRAL` — primarily factual with no meaningful positive/negative emotion
- `MIXED` — meaningful positive and negative sentiment appear together

Do not classify based on a single positive word without considering context. Sarcasm should be interpreted by meaning and flagged for review when uncertain.

## 3. Urgency

- `LOW` — general question, feedback, or non-time-sensitive issue
- `MEDIUM` — issue affects the customer and needs resolution but does not indicate immediate serious impact
- `HIGH` — explicit immediate deadline, account/security concern, repeated failed resolution, or serious time-sensitive impact

Do not infer HIGH urgency solely because a message is angry.

## 4. Requires Review

Set `TRUE` when:

- sarcasm makes sentiment uncertain;
- multiple categories are equally plausible;
- context is insufficient;
- the text is contradictory;
- a label requires an unsupported assumption.

Otherwise use `FALSE`.

## Quality Rules

1. Read the complete record before labeling.
2. Use only allowed taxonomy values.
3. Do not guess missing context.
4. Apply the same rule to similar records.
5. Flag uncertainty instead of forcing a confident label.
6. Review all `requires_review=TRUE` records before final dataset delivery.
