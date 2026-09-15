import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "retail_video_annotations.json"


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    classes = {int(k):v for k,v in data["classes"].items()}
    class_counts, states = Counter(), Counter()
    track_frames = defaultdict(set)
    total = review = occluded = 0

    for frame in data["frames"]:
        for ann in frame["annotations"]:
            total += 1
            class_counts[classes[ann["class_id"]]] += 1
            states[ann["state"]] += 1
            review += bool(ann["needs_review"])
            occluded += bool(ann["occluded"])
            track_frames[ann["track_id"]].add(frame["frame_id"])

    print(f"Frames: {len(data['frames'])}")
    print(f"Annotations: {total}")
    print(f"Unique tracks: {len(track_frames)}")
    print(f"Review rate: {review/total:.1%}")
    print(f"Occlusion rate: {occluded/total:.1%}")
    print("Class distribution:", dict(class_counts))
    print("State distribution:", dict(states))
    print("Track lengths:", {k:len(v) for k,v in track_frames.items()})


if __name__ == "__main__":
    main()
