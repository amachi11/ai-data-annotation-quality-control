import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "data" / "annotated_data.csv"
SECONDARY = ROOT / "data" / "second_annotator_sample.csv"
REPORT = ROOT / "reports" / "disagreement_report.csv"
FIELDS = ["category", "sentiment", "urgency"]


def load(path):
    with path.open(newline="", encoding="utf-8") as f:
        return {row["id"]: row for row in csv.DictReader(f)}


def cohen_kappa(a, b):
    if len(a) != len(b) or not a:
        return 0.0
    observed = sum(x == y for x, y in zip(a, b)) / len(a)
    labels = set(a) | set(b)
    ca, cb = Counter(a), Counter(b)
    expected = sum((ca[label] / len(a)) * (cb[label] / len(b)) for label in labels)
    if expected == 1:
        return 1.0
    return (observed - expected) / (1 - expected)


def main():
    primary, secondary = load(PRIMARY), load(SECONDARY)
    ids = sorted(set(primary) & set(secondary), key=int)
    disagreements = []

    for field in FIELDS:
        a = [primary[i][field] for i in ids]
        b = [secondary[i][field] for i in ids]
        agreement = sum(x == y for x, y in zip(a, b)) / len(ids)
        print(f"{field}: agreement={agreement:.1%}, kappa={cohen_kappa(a,b):.3f}")

        for i, x, y in zip(ids, a, b):
            if x != y:
                disagreements.append([i, field, x, y, primary[i]["text"]])

    REPORT.parent.mkdir(exist_ok=True)
    with REPORT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "field", "primary_label", "second_label", "text"])
        writer.writerows(disagreements)
    print(f"Disagreements exported: {len(disagreements)}")


if __name__ == "__main__":
    main()
