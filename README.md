# AI Data Annotation & Quality Control Portfolio

A practical portfolio project demonstrating proficiency in AI data annotation, labeling consistency, dataset validation, and quality control.

## Project Overview

This project simulates a real-world text annotation workflow for AI training data. Customer-support messages are labeled across four dimensions:

- **Category** — DELIVERY, BILLING, ACCOUNT, PRODUCT, OTHER
- **Sentiment** — POSITIVE, NEGATIVE, NEUTRAL, MIXED
- **Urgency** — LOW, MEDIUM, HIGH
- **Requires Review** — TRUE/FALSE for ambiguous or difficult records

A Python quality-control pipeline checks for invalid labels, missing values, inconsistent combinations, and records that require manual review.

## Skills Demonstrated

- AI data annotation and labeling
- Annotation guideline interpretation
- Label taxonomy design
- Edge-case and ambiguity handling
- Data validation and quality assurance
- Python scripting
- CSV dataset management
- Annotation consistency checks
- Quality reporting and review workflows

## Repository Structure

```text
ai-data-annotation-quality-control/
├── README.md
├── annotation_guidelines.md
├── requirements.txt
├── data/
│   ├── raw_data.csv
│   └── annotated_data.csv
├── src/
│   ├── validate_annotations.py
│   ├── quality_control.py
│   └── generate_report.py
├── reports/
│   └── annotation_quality_report.csv
└── examples/
    └── annotation_examples.md
```

## Annotation Workflow

1. Review each raw text record.
2. Apply labels using the project taxonomy.
3. Flag ambiguous, sarcastic, or unclear examples for human review.
4. Run validation to detect missing or invalid annotations.
5. Run quality-control rules to identify suspicious label combinations.
6. Generate a summary report for final review.

## Example Annotation

**Text:** `My order was supposed to arrive yesterday and I still don't have it.`

| Field | Label |
|---|---|
| Category | DELIVERY |
| Sentiment | NEGATIVE |
| Urgency | MEDIUM |
| Requires Review | FALSE |

## Quality-Control Approach

High-quality annotation is not simply assigning labels. It requires consistency, careful interpretation of guidelines, and a clear process for uncertainty. Ambiguous records should be flagged rather than guessed.

This project demonstrates that approach by separating straightforward annotations from records requiring review and applying automated validation before a dataset is considered complete.

## Running the Project

```bash
pip install -r requirements.txt
python src/validate_annotations.py
python src/quality_control.py
python src/generate_report.py
```

## Author

**Amanda Eze**  
AI Automation • Data Analysis • Data Annotation
