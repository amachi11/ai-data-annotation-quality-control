# Retail Image & Video Annotation Guidelines

## 1. Bounding Boxes

Draw the smallest axis-aligned rectangle that contains all visible pixels belonging to the target object. Do not include shadows or unnecessary surrounding background.

For partially occluded objects, box only the visible extent. Set `occluded=true` when another object blocks a meaningful portion of the target. Set `truncated=true` when the target extends beyond the image boundary.

## 2. Segmentation

Polygon points should follow the visible object boundary. Do not estimate invisible portions behind a hand, shelf edge, or another product. Use enough vertices to represent meaningful shape changes without adding redundant points.

## 3. Tracking

The same physical object must retain the same `track_id` across consecutive frames. Track IDs must never be reused for a different object in the same sequence.

Maintain identity through short occlusions only when the reappearing object can be identified confidently from motion, location, appearance, and context. If uncertain, start a new track and flag the transition for review.

## 4. Product/Hand Interactions

Product states:
- `on_shelf`
- `held`
- `in_basket`
- `unknown`

Hand actions:
- `reaching`
- `holding`
- `releasing`
- `other`

A product should change from `on_shelf` to `held` only when there is visual evidence of possession. Proximity alone is not sufficient.

## 5. Difficult Cases

Set `needs_review=true` for:
- severe occlusion where identity is uncertain;
- overlapping products that cannot be separated confidently;
- uncertain class assignment;
- possible track-ID switches;
- motion blur that prevents accurate boundaries;
- interaction states that cannot be determined from the visible frame(s).

## 6. Quality Standard

Before submission, verify:
1. every target object has the correct class;
2. boxes are tight and inside image boundaries;
3. track IDs remain consistent;
4. occlusion/truncation attributes are correct;
5. interaction labels match visible evidence;
6. uncertain examples are flagged instead of guessed.

## 7. Review Priority

Review order is: invalid geometry → possible track-ID switch → uncertain class → severe occlusion → uncertain interaction → minor boundary refinement.
