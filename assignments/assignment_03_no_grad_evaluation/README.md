# Assignment 3 — No-Grad Evaluation

## Purpose

Apply the BGR (Building Graph Representation) workflow to an original Rhino pilotis model.
Build a BGR graph dataset following S06-13A, then run no-gradient inference with the pretrained
`bgr_model.pt` following S06-13B. The model classifies the building into one of five pilotis
typologies.

## Run order

```
1. Model the building in Rhino. Export four OBJ files to 01_input_graph/:
      ground.obj, columns.obj, offices.obj, core.obj

2. Set the label in 01_input_graph/dataset/graphs.csv to the student's own typological
   assessment (0=Separation, 1=Separation with Plinth, 2=Adherence,
   3=Adherence with Plinth, 4=Interlock).
   Current file value: label=0 (student manual assessment: Separation)

3. 02_notebook_work/A3_01_BGR_Graph_Creation.ipynb
      Follows S06-13A. Builds the BGR graph from OBJ geometry.
      -> reads:   01_input_graph/ground.obj
                  01_input_graph/columns.obj
                  01_input_graph/offices.obj
                  01_input_graph/core.obj
      -> writes:  01_input_graph/dataset/nodes.csv
                  01_input_graph/dataset/edges.csv
                  01_input_graph/dataset/graphs.csv
                  01_input_graph/dataset/meta.yaml

4. 02_notebook_work/A3_02_No_Grad_Prediction.ipynb
      Follows S06-13B. Loads model and runs inference.
      -> reads:   01_input_graph/dataset/
                  ../../shared/assets/course_supporting_files/bgr_model.pt
      -> writes:  03_predictions/predictions.csv
                  04_visuals/01_bgr_prediction.png
                  04_visuals/02_bgr_prediction_detail.png
```

## Inputs

| File | Path | Status |
|------|------|--------|
| `ground.obj` | `01_input_graph/` | Present |
| `columns.obj` | `01_input_graph/` | Present |
| `offices.obj` | `01_input_graph/` | Present |
| `core.obj` | `01_input_graph/` | Present |
| `Rhino.3dm` | `00_brief_and_references/` | Present |
| `bgr_model.pt` | `../../shared/assets/course_supporting_files/` | Present — 34.8 MB pretrained |

## Outputs

Nodes CSV feature columns produced by `Graph.ExportToCSV` (TopologicPy prepends `feat_` to each key):

| CSV column | Spatial category |
|------------|-----------------|
| `feat_feature_00` | ground slab |
| `feat_feature_01` | column |
| `feat_feature_02` | plinth |
| `feat_feature_03` | office / residential massing |
| `feat_feature_04` | core |

A3_02 validation cell (`c_validate`) confirms these exact column names before loading the dataset.

| File | Path | Status |
|------|------|--------|
| `nodes.csv` | `01_input_graph/dataset/` | Present — feat_feature_00..04 schema |
| `edges.csv` | `01_input_graph/dataset/` | Present |
| `graphs.csv` | `01_input_graph/dataset/` | Present — label=0 (student manual: Separation) |
| `meta.yaml` | `01_input_graph/dataset/` | Present |
| `predictions.csv` | `03_predictions/` | Present — pred_label=1 (Separation with Plinth) |
| `01_bgr_prediction.png` | `04_visuals/` | Present — class probability bar chart |
| `02_bgr_prediction_detail.png` | `04_visuals/` | Present — annotated BGR diagram |
| `05_submission_text/` | — | Empty — written interpretation pending |

Prediction detail from `03_predictions/predictions.csv`:

```
graph_idx : 0
pred_label: 1  — Separation with Plinth   (model prediction)
prob_0    : 3.1e-06  (Separation)
prob_1    : 0.9999   (Separation with Plinth)
prob_2    : 1.4e-08  (Adherence)
prob_3    : 1.8e-05  (Adherence with Plinth)
prob_4    : 4.2e-06  (Interlock)

Student manual label (graphs.csv) : 0 — Separation
Model prediction                  : 1 — Separation with Plinth
Result: the manual label and the model prediction differ.
```

## Submission evidence

| Deliverable | Status |
|------------|--------|
| A3_01 notebook | Present — SelfMerge, 5-feature one-hot, ExportToCSV |
| A3_02 notebook | Present — categorical labels, c_validate, c_deps, prediction |
| Four OBJ inputs | Present in `01_input_graph/` |
| `01_input_graph/dataset/nodes.csv` | Present |
| `01_input_graph/dataset/edges.csv` | Present |
| `01_input_graph/dataset/graphs.csv` | Present |
| `01_input_graph/dataset/meta.yaml` | Present |
| `03_predictions/predictions.csv` | Present |
| `04_visuals/01_bgr_prediction.png` | Present |
| `04_visuals/02_bgr_prediction_detail.png` | Present |
| Written interpretation | Pending — `05_submission_text/` is empty |

## Known limitations

1. **Written interpretation absent.** `05_submission_text/` is empty. Produce a written
   spatial interpretation of the prediction result, including discussion of the label
   discrepancy, before submission.

2. **Manual label and prediction differ.** The student recorded `label=0` (Separation) in
   `graphs.csv`. The model predicts `label=1` (Separation with Plinth). The written
   interpretation must address this discrepancy.

3. **Plinth geometry absent from OBJ exports.** The five-category schema includes plinth
   (category 2) but no `plinth.obj` was exported. If the building has a plinth element,
   export a separate `plinth.obj` and integrate it in A3_01 before regenerating the dataset.

## Current status

All four OBJ inputs present. BGR dataset generated and validated. Prediction complete.
Both visual outputs (`01_bgr_prediction.png`, `02_bgr_prediction_detail.png`) present.
Written interpretation in `05_submission_text/` is pending.

Course reference notebooks: `../../class_notebooks/S06_graph_ml/`
(S06-13A GML Creating BGR Graph — STUDENT, S06-13B GML Predict BGR Graph)
