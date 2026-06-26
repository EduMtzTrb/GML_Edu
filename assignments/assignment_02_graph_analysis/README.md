# Assignment 2 — Graph Analysis

## Goal

Compute graph-theoretic metrics on the spatial graph produced in Assignment 1 and
interpret each metric in terms of architectural and spatial meaning.

## Source notebooks (read-only references)

| Notebook | Session | Purpose |
|----------|---------|---------|
| `S03-07 Spatial Intelligence Part 1.ipynb` | S03 | Degree, betweenness, clustering |
| `S03-08 Spatial Intelligence Part 2.ipynb` | S03 | Graph diameter, shortest paths |
| `S03-09 Spatial Intelligence Part 3.ipynb` | S03 | Metric interpretation and comparison |

Course notebooks are in `../../class_notebooks/S03_graph_analysis/`.

## Inputs

| File | Source | Status |
|------|--------|--------|
| `nodes.csv` | Assignment 1 output (`../assignment_01_graph_generation/04_graph_dataset/`) | Not yet produced |
| `edges.csv` | Assignment 1 output (same) | Not yet produced |

Copy or symlink the Assignment 1 outputs into `01_input_graph/` before running.

## Expected outputs

| File | Location | Description |
|------|----------|-------------|
| `metrics_table.csv` | `03_results/` | Per-node metric values (degree, betweenness, clustering, etc.) |
| Graph metric charts | `04_visuals/` | Distribution plots, annotated graph views |
| Written interpretation | `05_submission_text/` | Spatial meaning of each metric |

## Run order

```
1. Complete Assignment 1 first — produces nodes.csv and edges.csv
2. Copy outputs to 01_input_graph/
3. 02_notebook_work/A2_01_[name].ipynb — metric computation
4. 02_notebook_work/A2_02_[name].ipynb — visualisation and interpretation
```

## Current status

**Not started.** Waiting on Assignment 1 graph dataset.

## Folder contents

| Folder | Contents |
|--------|----------|
| `00_brief_and_references/` | Empty — add brief PDF and reference notes here |
| `01_input_graph/` | Empty — copy nodes.csv and edges.csv from Assignment 1 here |
| `02_notebook_work/` | Empty — analysis notebooks go here |
| `03_results/` | Empty — metric CSV outputs |
| `04_visuals/` | Empty — chart PNG outputs |
| `05_submission_text/` | Empty — written interpretation |
