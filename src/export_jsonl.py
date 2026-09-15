import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "annotated_data.csv"
OUTPUT = ROOT / "data" / "training_data.jsonl"


def main():
    with SOURCE.open(newline="", encoding="utf-8") as src, OUTPUT.open("w", encoding="utf-8") as out:
        for row in csv.DictReader(src):
            record = {
                "id": int(row["id"]),
                "text": row["text"],
                "labels": {
                    "category": row["category"],
                    "sentiment": row["sentiment"],
                    "urgency": row["urgency"],
                },
                "requires_review": row["requires_review"] == "TRUE",
                "reviewer_note": row.get("reviewer_note", ""),
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"Exported JSONL training data to {OUTPUT}")


if __name__ == "__main__":
    main()
