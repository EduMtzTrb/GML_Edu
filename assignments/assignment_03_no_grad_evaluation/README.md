# Assignment 3 — No-Grad Evaluation

## Goal

Apply the BGR (Building Graph Representation) workflow to an original Rhino model:
build the graph dataset using S06-13A, then run no-gradient inference with the
pretrained `bgr_model.pt` using S06-13B.

## Source notebooks (read-only references)

| Notebook | Session | Purpose |
|----------|---------|---------|
| `S06-13 GML Graph Classification.ipynb` | S06 | Full classification pipeline (background) |
| `S06-13A GML Creating BGR Graph - STUDENT.ipynb` | S06 | **Primary:** OBJ to BGR graph dataset |
| `S06-13B GML Predict BGR Graph.ipynb` | S06 | **Primary:** No-grad inference with bgr_model.pt |

Course notebooks are in `../../class_notebooks/S06_graph_ml/`.
Pretrained model: `../../shared/assets/course_supporting_files/bgr_model.pt`

## Inputs required

Four OBJ files exported from a Rhino BGR floor-plan model (one per spatial layer):

| File | Spatial layer | Status |
|------|--------------|--------|
| `ground.obj` | Ground slab | Not yet exported from Rhino |
| `columns.obj` | Pilotis columns | Not yet exported from Rhino |
| `offices.obj` | Residential/program massing | Not yet exported from Rhino |
| `core.obj` | Vertical core per floor | Not yet exported from Rhino |

OBJ files go in `01_input_graph/`. They must follow the BGR schema expected by `bgr_model.pt`.

## Expected outputs

| File | Location | Description |
|------|----------|-------------|
| `nodes.csv` | `01_input_graph/dataset/` | BGR graph node features |
| `edges.csv` | `01_input_graph/dataset/` | BGR graph edges |
| `graphs.csv` | `01_input_graph/dataset/` | Graph-level metadata |
| `meta.yaml` | `01_input_graph/dataset/` | Feature schema for the model |
| `predictions.csv` | `03_predictions/` | Predicted BGR labels per node |
| Graph visualisations | `04_visuals/` | Graph with predicted labels overlaid |

## Run order

```
1. Model BGR building in Rhino; export four OBJ files to 01_input_graph/
2. 02_notebook_work/A3_01_BGR_Graph_Creation.ipynb  (follows S06-13A)
      -> produces: 01_input_graph/dataset/nodes.csv, edges.csv, graphs.csv, meta.yaml
3. 02_notebook_work/A3_02_No_Grad_Prediction.ipynb  (follows S06-13B)
      -> produces: 03_predictions/predictions.csv
                   04_visuals/*.png
```

## Current status

**Not started.** Rhino OBJ exports not yet produced.

## Folder contents

| Folder | Contents |
|--------|----------|
| `00_brief_and_references/` | Empty — add brief and S06-13A/13B reference notes |
| `01_input_graph/` | Empty — four OBJ files + assembled dataset go here |
| `02_notebook_work/` | Empty — adaptation of S06-13A and S06-13B notebooks |
| `03_predictions/` | Empty — inference results from S06-13B |
| `04_visuals/` | Empty — graph and prediction visualisations |
| `05_submission_text/` | Empty — written interpretation |

## Reference material in archive

`archive/superseded_work/A1_01_DoubleL_BGR_Graph_Generation.ipynb` is an earlier
adaptation of S06-13A for the Double-L building. It demonstrates the BGR pipeline
on the resident_gen geometry and can serve as a concrete reference, but it uses
resident_gen exports (rooms/corridors/cores), not the four-OBJ BGR format that
`bgr_model.pt` expects. Read it for methodology, not for direct reuse.
