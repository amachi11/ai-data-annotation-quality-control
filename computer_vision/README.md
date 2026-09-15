# Retail Computer Vision Annotation & Tracking

Advanced portfolio module demonstrating a production-style annotation workflow for retail computer-vision datasets involving products, customer hands, shelves, baskets, and object interactions.

## Capabilities Demonstrated

- Bounding-box annotation
- Polygon/segmentation annotation schema
- Multi-object video tracking with persistent track IDs
- Occlusion and truncation handling
- Product/hand interaction labeling
- Frame-to-frame track consistency checks
- COCO-style export
- YOLO-format conversion
- Annotation quality assurance
- Bounding-box geometry validation
- IoU-based temporal consistency checks
- Dataset statistics and review queues

## Scenario

A retail vision system needs training data to recognize products and customer interactions across store-camera frames. Each visible object is assigned a class, geometry, attributes, and—when part of a video sequence—a persistent `track_id`.

### Classes

| ID | Class | Description |
|---|---|---|
| 0 | product | Retail item/product |
| 1 | hand | Customer or employee hand |
| 2 | basket | Shopping basket |
| 3 | shelf | Shelf/display region |

### Interaction attributes

Products may be labeled `on_shelf`, `held`, `in_basket`, or `unknown`. Hands may be labeled `reaching`, `holding`, `releasing`, or `other`.

## Annotation Rules

Bounding boxes should tightly enclose the visible object without unnecessary background. Objects that remain visible across adjacent frames retain the same track ID. Occluded objects remain tracked when identity can be established confidently. If identity becomes uncertain after a long/full occlusion, a new track is created rather than guessing.

Segmentation polygons follow visible object boundaries. Annotators should not hallucinate invisible boundaries behind occluders. Difficult examples are marked `needs_review=true` and routed to adjudication.

## Quality-Control Pipeline

`validate_cv_annotations.py` checks class IDs, box geometry, image boundaries, duplicate annotation IDs, required attributes, confidence ranges, and track metadata.

`track_quality_control.py` groups annotations by track ID and checks for class changes, impossible frame order, large frame-to-frame geometry jumps, and low IoU that may indicate an ID switch or poor box placement.

`convert_to_yolo.py` converts bounding boxes into normalized YOLO training labels.

`dataset_statistics.py` reports class balance, review rate, occlusion rate, interaction distribution, and track statistics.

## Structure

```text
computer_vision/
├── README.md
├── annotation_guidelines.md
├── data/
│   ├── classes.json
│   ├── retail_video_annotations.json
│   └── review_queue.csv
├── examples/
│   └── frame_annotation_examples.md
├── src/
│   ├── validate_cv_annotations.py
│   ├── track_quality_control.py
│   ├── convert_to_yolo.py
│   └── dataset_statistics.py
└── reports/
    └── cv_quality_report.md
```

## Portfolio Note

This module uses a synthetic annotation manifest to demonstrate the structure, reasoning, validation, and quality-control processes used in computer-vision annotation. It does not contain confidential employer/client imagery and is not represented as paid client work.
