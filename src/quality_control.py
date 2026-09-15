import csv
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "annotated_data.csv"


def qc_flags(row):
    flags = []
    text = row["text"].lower()

    if row["requires_review"] == "TRUE":
        flags.append("MANUAL_REVIEW")

    if row["urgency"] == "HIGH" and not any(
        term in text for term in ["today", "tomorrow", "deadline", "immediately", "urgent"]
    ):
        flags.append("CHECK_HIGH_URGENCY")

    if row["sentiment"] == "POSITIVE" and any(
        term in text for term in ["late", "broken", "charged twice", "can't", "stopped working"]
    ):
        flags.append("CHECK_SENTIMENT")

    if row["category"] == "DELIVERY" and not any(
        term in text for term in ["order", "package", "delivery", "tracking", "arrive"]
    ):
        flags.append("CHECK_DELIVERY_CATEGORY")

    return flags


def main():
    flagged = 0
    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    for row in rows:
        flags = qc_flags(row)
        if flags:
            flagged += 1
            print(f"Record {row['id']}: {', '.join(flags)}")

    print(f"QC complete: {len(rows)} records checked; {flagged} records flagged for review.")


if __name__ == "__main__":
    main()
