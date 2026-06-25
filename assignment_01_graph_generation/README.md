# Assignment 1 — Graph Generation

## Purpose

Convert an architectural floor plan modelled in Rhino into a spatial adjacency graph using TopologicPy, and export the result as structured CSV files.

## Expected inputs

- One or more OBJ files exported from Rhino representing the floor plan geometry (rooms, boundaries, or CellComplex layers).

## Expected outputs

- `outputs/nodes.csv` — one row per graph node; columns include node ID and spatial feature values.
- `outputs/edges.csv` — one row per edge; columns include source and target node IDs.
- `visuals/` — graph visualisation plots generated inside the notebook.

## Folder contents

| Folder | Contents |
|---|---|
| `assets/` | Source OBJ files exported from Rhino |
| `notebooks/` | Working Jupyter notebook(s) |
| `outputs/` | CSV graph data |
| `visuals/` | Graph plots and diagrams |
| `docs/` | Methodology notes |

## Current status

**Not started.**
