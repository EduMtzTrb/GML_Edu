# Assignment 1 — Graph Generation

## Purpose

Derive a spatial room-and-circulation graph from architectural OBJ geometry using TopologicPy,
following the S02 course workflow. Three Two-Bars building layouts (BB_01, BB_02, BB_03) are
each processed into a graph CSV dataset and a set of visualisations.

## Run order

```
1. 02_notebook_work/A1_01_TwoBars_Geometry_to_Graph.ipynb
      Set LAYOUT_ID = "BB_01", "BB_02", or "BB_03". Run once per building.
      -> reads:   ../../shared/assets/resident_gen/Exports/BB_XX/
      -> writes:  03_graph_dataset/BB_XX/nodes.csv
                  03_graph_dataset/BB_XX/edges.csv
                  04_visuals/BB_XX/BB_XX_01_spatial_adjacency_graph.png

2. 02_notebook_work/A1_02_TwoBars_Graph_Visualisation_and_Export.ipynb
      Set LAYOUT_ID = "BB_01", "BB_02", or "BB_03". Run once per building.
      -> reads:   03_graph_dataset/BB_XX/
      -> writes:  04_visuals/BB_XX/BB_XX_02_graph_by_type.png
                  04_visuals/BB_XX/BB_XX_03_graph_by_physical_floor.png
                  04_visuals/BB_XX/BB_XX_04_graph_by_apartment.png
                  04_visuals/BB_XX/BB_XX_05_degree_distribution.png
                  04_visuals/BB_XX/BB_XX_assignment1_report_summary.txt

3. 02_notebook_work/A1_03_TwoBars_BB_Visual_Comparison.ipynb
      Reads all three BBs. No LAYOUT_ID setting required.
      -> reads:   03_graph_dataset/BB_01/, BB_02/, BB_03/
      -> writes:  04_visuals/BB_comparison/
```

## Inputs

| Path | Contents |
|------|----------|
| `../../shared/assets/resident_gen/Exports/BB_01/` | BB_01 OBJ files (rooms, corridors, cores, metadata) |
| `../../shared/assets/resident_gen/Exports/BB_02/` | BB_02 OBJ files |
| `../../shared/assets/resident_gen/Exports/BB_03/` | BB_03 OBJ files |
| `01_brief_and_references/OBJ_EXPORTER_USAGE.md` | OBJ export instructions |
| `01_brief_and_references/topologicpy_obj_exporter.py` | Export helper script |

## Outputs

**nodes.csv columns (14):**
`layout_id, node_id, node_name, node_role, space_type, zone_type, apartment_id, floor_id, physical_floor, area, volume, X, Y, Z`

**edges.csv columns (8):**
`layout_id, src_id, dst_id, edge_type, contact_axis, gap_m, shared_span_m, physical_floor`

| Path | Contents |
|------|----------|
| `03_graph_dataset/BB_01/` | nodes.csv (175 nodes), edges.csv (388 edges) |
| `03_graph_dataset/BB_02/` | nodes.csv (381 nodes), edges.csv (858 edges) |
| `03_graph_dataset/BB_03/` | nodes.csv (141 nodes), edges.csv (303 edges) |
| `04_visuals/BB_01/` | 9 PNGs: graph views 01–05, Rhino screenshots 06–09; report .txt |
| `04_visuals/BB_02/` | 9 PNGs: graph views 01–05, Rhino screenshots 06–09; report .txt |
| `04_visuals/BB_03/` | 9 PNGs: graph views 01–05, Rhino screenshots 06–09; report .txt |
| `04_visuals/BB_comparison/` | Cross-building dashboards and summary CSVs |
| `05_submission_text/` | Empty — written interpretation pending |

## Submission evidence

| File | Status |
|------|--------|
| `03_graph_dataset/BB_01/nodes.csv` | Present — 175 nodes |
| `03_graph_dataset/BB_01/edges.csv` | Present — 388 edges |
| `03_graph_dataset/BB_02/nodes.csv` | Present — 381 nodes |
| `03_graph_dataset/BB_02/edges.csv` | Present — 858 edges |
| `03_graph_dataset/BB_03/nodes.csv` | Present — 141 nodes |
| `03_graph_dataset/BB_03/edges.csv` | Present — 303 edges |
| `04_visuals/BB_01/` | Present — 5 graph PNGs (01–05), 4 Rhino screenshots (06–09), report .txt |
| `04_visuals/BB_02/` | Present — 5 graph PNGs (01–05), 4 Rhino screenshots (06–09), report .txt |
| `04_visuals/BB_03/` | Present — 5 graph PNGs (01–05), 4 Rhino screenshots (06–09), report .txt |
| `04_visuals/BB_comparison/` | Present — scale dashboard, role comparison, per-view overlays, CSVs |
| `05_submission_text/` | Empty — written interpretation pending |

## Known limitations

1. **Bounding-box adjacency workaround.** `BB_XX_doors.obj` is empty in the resident_gen exports.
   The notebook uses bounding-box spatial adjacency with a 0.45 m gap tolerance instead of
   face-shared or door-access edges. Some cross-wall false adjacencies may appear; some
   close-but-disconnected rooms may be missed.

2. **No inter-floor edges.** Stair and lift connector geometry is absent from the exports.
   Vertical circulation is not represented in the graph.

3. **Disconnected per-floor components.** Each physical floor is a separate connected component.
   Cross-floor graph metrics are computed per component in Assignment 2.

## Current status

All three buildings fully processed. Datasets, graph visualisations, and Rhino screenshots
are present for BB_01, BB_02, and BB_03. Written interpretation in `05_submission_text/` is pending.

Course reference notebooks: `../../class_notebooks/S02_geometry_to_topology/`
(S02-01 Primal vs Dual, S02-06 Importing OBJ files)
