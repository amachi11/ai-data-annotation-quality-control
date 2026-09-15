# Computer Vision Annotation QC Report

## Dataset Summary

- Scenario: retail product/customer-hand interaction sequence
- Frames represented: 6
- Object classes: product, hand, basket, shelf
- Persistent tracks represented: product #10, hand #20, basket #30
- Annotation geometry: bounding boxes + visible-boundary polygons
- Review attributes: confidence, occlusion, truncation, interaction state, needs-review flag

## Sequence Demonstrated

The sample sequence follows a product from `on_shelf` through customer reach, hand contact, `held`, release, and `in_basket`. Product and hand identities remain associated with persistent track IDs across frames.

## QA Checks

- Schema and required-field validation
- Unique annotation IDs
- Class-ID validation
- Bounding-box boundary validation
- Positive box dimensions
- Polygon structure validation
- Confidence range validation
- Track class consistency
- Frame ordering
- IoU-based temporal track checks
- Manual review routing

## Difficult Case

Frame 104 marks the product as `needs_review=true` because the product is significantly occluded during the hand interaction and its confidence is lower than neighboring frames. This demonstrates an explicit review workflow rather than forcing certainty.

## Export Readiness

The repository includes a converter for normalized YOLO bounding-box labels. The source JSON also preserves richer metadata—segmentation, track IDs, occlusion, interaction state, and confidence—that would otherwise be lost in a simple YOLO detection label.

## Integrity Note

This is a synthetic portfolio demonstration of a computer-vision annotation workflow. It is designed to demonstrate annotation reasoning, schema design, tracking, export, and quality-control skills without using confidential client data.
