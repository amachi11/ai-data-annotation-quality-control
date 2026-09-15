import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "annotated_data.csv"
OUT_DIR = ROOT / "data" / "splits"
SEED = 42


def write_csv(path, rows, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    with SOURCE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    rng = random.Random(SEED)
    rng.shuffle(rows)
    n = len(rows)
    train_end = round(n * 0.70)
    val_end = train_end + round(n * 0.15)

    splits = {
        "train.csv": rows[:train_end],
        "validation.csv": rows[train_end:val_end],
        "test.csv": rows[val_end:],
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, split_rows in splits.items():
        write_csv(OUT_DIR / name, split_rows, fieldnames)
        print(f"{name}: {len(split_rows)} records")


if __name__ == "__main__":
    main()
