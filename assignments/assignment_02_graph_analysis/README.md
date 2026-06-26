# Assignment 2 — Graph Analysis

## Purpose

Compute graph-theoretic metrics on the spatial graphs produced in Assignment 1 and interpret
each metric in terms of architectural and spatial meaning. Three Two-Bars layouts (BB_01,
BB_02, BB_03) are analysed and compared.

## Run order

```
1. 02_notebook_work/A2_01_TwoBars_Graph_Metrics.ipynb
      Set LAYOUT_ID = "BB_01", "BB_02", or "BB_03". Run once per building.
      -> reads:   ../assignment_01_graph_generation/04_graph_dataset/BB_XX/nodes.csv
                  ../assignment_01_graph_generation/04_graph_dataset/BB_XX/edges.csv
      -> writes:  03_results/BB_XX/metrics_table.csv
                  03_results/BB_XX/graph_summary.csv
                  03_results/BB_XX/community_summary.csv
                  03_results/BB_XX/component_summary.csv
                  03_results/BB_comparison.csv
                  04_visuals/BB_XX/01_degree_centrality.png
                  04_visuals/BB_XX/02_betweenness_centrality.png
                  04_visuals/BB_XX/03_closeness_centrality.png
                  04_visuals/BB_XX/04_clustering_coefficient.png
                  04_visuals/BB_XX/05_community_detection.png

2. 02_notebook_work/A2_02_TwoBars_Spatial_Interpretation.ipynb
      Set LAYOUT_ID = "BB_01", "BB_02", or "BB_03". Run once per building.
      -> reads:   03_results/BB_XX/
      -> writes:  04_visuals/BB_XX/06_composite_metric_panel.png
                  04_visuals/BB_XX/07_metrics_by_role.png
                  04_visuals/BB_XX/08_floor_metric_profile.png
                  04_visuals/BB_XX/09_metric_correlation.png
                  04_visuals/BB_comparison_overview.png
                  05_submission_text/BB_XX/interpretation.md
```

## Inputs

| Path | Contents |
|------|----------|
| `../assignment_01_graph_generation/04_graph_dataset/BB_01/` | nodes.csv, edges.csv |
| `../assignment_01_graph_generation/04_graph_dataset/BB_02/` | nodes.csv, edges.csv |
| `../assignment_01_graph_generation/04_graph_dataset/BB_03/` | nodes.csv, edges.csv |

`01_input_graph/` is reserved for manual copies; notebooks read directly from Assignment 1 output paths.

## Outputs

| Path | Contents |
|------|----------|
| `03_results/BB_01/` | metrics_table.csv (175 rows), graph_summary.csv, community_summary.csv, component_summary.csv |
| `03_results/BB_02/` | metrics_table.csv (381 rows), graph_summary.csv, community_summary.csv, component_summary.csv |
| `03_results/BB_03/` | metrics_table.csv (141 rows), graph_summary.csv, community_summary.csv, component_summary.csv |
| `03_results/BB_comparison.csv` | Cross-building metric summary |
| `04_visuals/BB_01/` | 9 metric PNGs (01–09) |
| `04_visuals/BB_02/` | 5 metric PNGs (01–05); extended visuals 06–09 pending |
| `04_visuals/BB_03/` | 5 metric PNGs (01–05); extended visuals 06–09 pending |
| `04_visuals/BB_comparison_overview.png` | Cross-building comparison panel |
| `05_submission_text/BB_01/interpretation.md` | Written spatial interpretation (BB_01 only) |

## Submission evidence

| File | Status |
|------|--------|
| `03_results/BB_01/metrics_table.csv` | Present — 175 rows |
| `03_results/BB_02/metrics_table.csv` | Present — 381 rows |
| `03_results/BB_03/metrics_table.csv` | Present — 141 rows |
| `03_results/BB_01/graph_summary.csv` | Present |
| `03_results/BB_02/graph_summary.csv` | Present |
| `03_results/BB_03/graph_summary.csv` | Present |
| `03_results/BB_01/community_summary.csv` | Present |
| `03_results/BB_02/community_summary.csv` | Present |
| `03_results/BB_03/community_summary.csv` | Present |
| `03_results/BB_01/component_summary.csv` | Present |
| `03_results/BB_02/component_summary.csv` | Present |
| `03_results/BB_03/component_summary.csv` | Present |
| `03_results/BB_comparison.csv` | Present |
| `04_visuals/BB_01/01–09_*.png` | Present — 9 metric PNGs |
| `04_visuals/BB_02/01–05_*.png` | Present — 5 metric PNGs |
| `04_visuals/BB_03/01–05_*.png` | Present — 5 metric PNGs |
| `04_visuals/BB_comparison_overview.png` | Present |
| `05_submission_text/BB_01/interpretation.md` | Present — BB_01 written interpretation |
| `05_submission_text/BB_02/` | Missing — interpretation pending |
| `05_submission_text/BB_03/` | Missing — interpretation pending |

## Known limitations

1. **Disconnected per-floor components.** Each physical floor is a separate connected component
   (no inter-floor edges in Assignment 1). Betweenness centrality is computed per component.
   Closeness centrality uses Wasserman-Faust normalisation for disconnected graphs.

2. **BB_02 and BB_03 extended visuals incomplete.** Composite metric panel, metrics-by-role,
   floor metric profile, and metric correlation charts exist for BB_01 only. Rerun A2_02 with
   `LAYOUT_ID = "BB_02"` and `"BB_03"` to produce the remaining charts.

3. **Written interpretation covers BB_01 only.** `05_submission_text/BB_01/interpretation.md`
   is complete. Interpretation files for BB_02 and BB_03 are pending.

## Current status

All three buildings: metrics computed, four results CSVs present, basic visuals (01–05) present.
BB_01: fully complete — extended visuals (06–09) and written interpretation present.
BB_02, BB_03: require a second A2_02 pass for extended visuals and written interpretation.

Course reference notebooks: `../../class_notebooks/S03_graph_analysis/`
(S03-07 Spatial Intelligence Part 1, S03-08 Part 2, S03-09 Part 3)
