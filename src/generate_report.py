import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "annotated_data.csv"
REPORT_FILE = ROOT / "reports" / "annotation_quality_report.csv"


def main():
    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    categories = Counter(row["category"] for row in rows)
    sentiments = Counter(row["sentiment"] for row in rows)
    review_count = sum(row["requires_review"] == "TRUE" for row in rows)

    report_rows = [
        ["metric", "value"],
        ["total_records", len(rows)],
        ["records_requiring_review", review_count],
        ["review_rate_percent", round(review_count / len(rows) * 100, 2)],
    ]

    for label, count in sorted(categories.items()):
        report_rows.append([f"category_{label.lower()}", count])
    for label, count in sorted(sentiments.items()):
        report_rows.append([f"sentiment_{label.lower()}", count])

    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with REPORT_FILE.open("w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerows(report_rows)

    print(f"Report written to {REPORT_FILE}")


if __name__ == "__main__":
    main()
