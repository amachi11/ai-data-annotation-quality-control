# AI Data Annotation & Quality Control Portfolio

An end-to-end portfolio project demonstrating AI training-data annotation, multi-label taxonomy design, confidence scoring, edge-case handling, dataset validation, quality assurance, agreement measurement, and train/validation/test preparation.

## Project Overview

This project simulates a production-style text annotation workflow for customer-support AI. Records are labeled across multiple dimensions:

- **Category** — DELIVERY, BILLING, ACCOUNT, PRODUCT, OTHER
- **Sentiment** — POSITIVE, NEGATIVE, NEUTRAL, MIXED
- **Urgency** — LOW, MEDIUM, HIGH
- **Confidence** — annotator confidence from 0.00 to 1.00
- **Requires Review** — TRUE/FALSE for ambiguous or difficult records

The workflow combines human annotation decisions with automated Python quality checks. It demonstrates how labeled data can move from raw input through annotation, validation, disagreement review, and ML-ready dataset splitting.

## Advanced Skills Demonstrated

- AI data annotation and multi-field labeling
- Annotation guideline and taxonomy design
- Confidence scoring
- Edge-case, sarcasm, and ambiguity handling
- Annotation quality assurance
- Inter-annotator agreement using Cohen's kappa
- Automated error and consistency detection
- Python-based dataset validation
- JSONL and CSV training-data export
- Reproducible train/validation/test splitting
- Dataset statistics and QC reporting

## Repository Structure

```text
ai-data-annotation-quality-control/
├── README.md
├── annotation_guidelines.md
├── requirements.txt
├── data/
│   ├── raw_data.csv
│   ├── annotated_data.csv
│   ├── second_annotator_sample.csv
│   └── training_data.jsonl
├── src/
│   ├── validate_annotations.py
│   ├── quality_control.py
│   ├── agreement_analysis.py
│   ├── export_jsonl.py
│   ├── split_dataset.py
│   └── generate_report.py
├── reports/
│   ├── annotation_quality_report.csv
│   └── disagreement_report.csv
└── examples/
    └── annotation_examples.md
```

## Annotation Workflow

1. Define the labeling taxonomy and edge-case rules.
2. Review each raw record and assign category, sentiment, urgency, and confidence.
3. Flag uncertain, sarcastic, contradictory, or multi-intent records for human review.
4. Validate required fields and allowed values programmatically.
5. Run QC rules to detect suspicious label combinations.
6. Compare a second annotation pass and calculate agreement.
7. Review disagreements rather than silently overwriting them.
8. Export the approved data to JSONL.
9. Create reproducible train/validation/test splits for downstream ML use.
10. Generate a QC summary report.

## Why Confidence Scores Matter

A label can be valid while still being uncertain. Confidence scoring makes that uncertainty visible. Low-confidence records can be prioritized for review instead of being treated as equally reliable training examples.

## Inter-Annotator Agreement

The project includes an independent second-pass annotation sample and a Cohen's kappa implementation. Agreement metrics help distinguish true labeling consistency from agreement that could occur by chance. Disagreements are exported for adjudication.

## Quality-Control Approach

High-quality annotation is not simply assigning labels. It requires consistency, traceability, careful guideline interpretation, and a defined process for uncertainty. The pipeline therefore checks schema validity, confidence ranges, review-note requirements, suspicious urgency/sentiment combinations, and annotator disagreements before data is considered ready for training.

## Running the Project

```bash
python src/validate_annotations.py
python src/quality_control.py
python src/agreement_analysis.py
python src/export_jsonl.py
python src/split_dataset.py
python src/generate_report.py
```

The project intentionally uses only the Python standard library so the workflow is easy to inspect and reproduce.

## Portfolio Note

This is a portfolio demonstration built to show annotation and AI training-data proficiency. It does not contain confidential client or employer data.

## Author

**Amanda Eze**  
AI Automation • Data Analysis • Data Annotation
