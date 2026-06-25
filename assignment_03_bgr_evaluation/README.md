# Assignment 3 — BGR Evaluation

## Purpose

Evaluate a pretrained Bedroom / Guest room / Reception (BGR) classifier against an original Rhino model, following the two-part course workflow: graph creation (13A) and no-gradient prediction (13B).

## Expected inputs

- Four OBJ files exported from a Rhino BGR floor-plan model (one per spatial layer, e.g., ground, columns, core, rooms).
- Pretrained model weights: `bgr_model.pt` (from course supporting files; not to be retrained).

## Expected outputs

- `dataset/` — graph feature dataset (nodes.csv, edges.csv, meta.yaml) assembled in the 13A notebook.
- `outputs/` — predicted room-type labels (BGR) produced by the 13B no-grad inference notebook.
- `visuals/` — graph plots and prediction result visualisations.

## Folder contents

| Folder | Contents |
|---|---|
| `assets/` | Four OBJ files from Rhino |
| `notebooks/` | 13A graph creation notebook; 13B prediction notebook |
| `dataset/` | Assembled feature dataset (CSV + YAML) |
| `outputs/` | Inference results |
| `visuals/` | Graph and prediction plots |
| `docs/` | Notes on model input requirements and feature schema |

## Current status

**Not started.**
