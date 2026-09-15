import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "retail_video_annotations.json"
OUT = ROOT / "data" / "yolo_labels"


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    W, H = data["image_width"], data["image_height"]
    OUT.mkdir(parents=True, exist_ok=True)
    for frame in data["frames"]:
        lines = []
        for ann in frame["annotations"]:
            x,y,w,h = ann["bbox"]
            xc, yc = (x+w/2)/W, (y+h/2)/H
            lines.append(f"{ann['class_id']} {xc:.6f} {yc:.6f} {w/W:.6f} {h/H:.6f}")
        (OUT / (Path(frame["file_name"]).stem + ".txt")).write_text("\n".join(lines)+"\n", encoding="utf-8")
    print(f"YOLO labels exported for {len(data['frames'])} frames to {OUT}")


if __name__ == "__main__":
    main()
