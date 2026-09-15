import csv
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "annotated_data.csv"

ALLOWED = {
    "category": {"DELIVERY", "BILLING", "ACCOUNT", "PRODUCT", "OTHER"},
    "sentiment": {"POSITIVE", "NEGATIVE", "NEUTRAL", "MIXED"},
    "urgency": {"LOW", "MEDIUM", "HIGH"},
    "requires_review": {"TRUE", "FALSE"},
}


def validate_row(row):
    errors = []
    required = ["id", "text", "category", "sentiment", "urgency", "requires_review"]

    for field in required:
        if not row.get(field, "").strip():
            errors.append(f"missing {field}")

    for field, valid_values in ALLOWED.items():
        if row.get(field) not in valid_values:
            errors.append(f"invalid {field}: {row.get(field)!r}")

    if row.get("requires_review") == "TRUE" and not row.get("reviewer_note", "").strip():
        errors.append("review flag requires reviewer_note")

    return errors


def main():
    total = 0
    invalid = 0

    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            total += 1
            errors = validate_row(row)
            if errors:
                invalid += 1
                print(f"Record {row.get('id')}: " + "; ".join(errors))

    print(f"Validated {total} records.")
    print(f"Valid: {total - invalid} | Invalid: {invalid}")

    if invalid:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
