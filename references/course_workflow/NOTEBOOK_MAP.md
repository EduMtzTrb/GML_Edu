# Notebook Map

This file maps course notebooks to the assignment they support. All notebooks are located in `references/Graph ML -- NOTEBOOKS/`. They are read-only references.

---

## Assignment 1 — Graph Generation

**Primary reference notebook:** `S02-06 Importing OBJ files.ipynb`

Purpose: demonstrates loading an OBJ file into TopologicPy, building a CellComplex, and extracting an adjacency graph. This is the foundational workflow for Assignment 1.

Supporting context:
- `S02-01` through `S02-05` — graph theory foundations (primal/dual, metric/topological, adjacency/access, geometric and spatial representations).
- `S03-07`, `S03-08`, `S03-09` — spatial intelligence notebooks extending graph construction and metric analysis.

---

## Assignment 2 — Graph Analysis

**Primary reference:** `S03-07 Spatial Intelligence Part 1.ipynb` and the Aditya student notebook (external, read-only).

Purpose: graph metric computation (degree centrality, betweenness, clustering coefficient, diameter) mapped to spatial meaning. The Aditya notebook is a student example demonstrating one complete metric analysis workflow.

Note: The Aditya notebook is in an external repository. Observe structure and methodology only; do not copy content.

---

## Assignment 3 — BGR Evaluation (13A and 13B)

**13A — Graph creation:** `S06-13A GML Creating BGR Graph - STUDENT.ipynb`

Purpose: student-facing notebook for loading four OBJ files, constructing the BGR graph, and assembling the feature dataset. This is the notebook to adapt with own geometry.

**13B — No-grad prediction:** `S06-13B GML Predict BGR Graph.ipynb`

Purpose: loads `bgr_model.pt` and runs `torch.no_grad()` inference on the graph produced in 13A. Output is predicted room-type labels (Bedroom / Guest room / Reception).

Supporting context:
- `S06-13 GML Graph Classification.ipynb` — full classification pipeline for background understanding.
- `references/Graph ML -- NOTEBOOKS/Supporting Files/bgr_model.pt` — pretrained model weights.
- `references/Graph ML -- NOTEBOOKS/Supporting Files/` — sample OBJ files (columns, core, ground, offices) showing expected geometry structure.

---

## Final Project — Room-Type Node Classification

**Primary reference:** `S06-15 GML Node Classification.ipynb`

Purpose: node-level classification workflow; predicts room type for each node in a floor-plan graph. Adapt this notebook to classify rooms in the two final-project typologies (two bars, two L-shaped blocks).

Supporting context:
- `S05-12 Dataset and Feature Engineering.ipynb` — feature engineering methodology applicable to the final-project dataset.
- `references/Graph ML -- NOTEBOOKS/Supporting Files/dataset_node_classification/` — example dataset schema (nodes.csv, edges.csv, graphs.csv, meta.yaml).
