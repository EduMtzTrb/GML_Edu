# Assignment 1 — Graph Generation

## Goal

Derive a spatial graph from architectural room geometry using TopologicPy,
following the S02 course workflow. Nodes represent rooms and circulation elements;
edges represent shared-face spatial adjacency (door-access workaround — see Blockers).

## Source notebooks (read-only references)

| Notebook | Session | Purpose |
|----------|---------|---------|
| `S02-01 Primal vs Dual.ipynb` | S02 | CellComplex.ByCells, Graph.ByTopology(direct=True) |
| `S02-03 Adjacency Vs Access.ipynb` | S02 | Aperture-based access graph (requires door geometry) |
| `S02-04 Geometric Representations.ipynb` | S02 | Graph.BySpatialRelationships |
| `S02-06 Importing OBJ files.ipynb` | S02 | Topology.ByOBJPath, OBJ loading pattern |

Course notebooks are in `../../class_notebooks/S02_geometry_to_topology/`.

## Inputs

| File | Location | Status |
|------|----------|--------|
| `TB_01_rooms.obj` | `../../shared/assets/resident_gen/Exports/TB_01/` | Available (573 rooms) |
| `TB_01_corridors.obj` | same | Available (20 corridors) |
| `TB_01_cores.obj` | same | Available (3 cores) |
| `TB_01_doors.obj` | same | **EMPTY — 0 door objects** |
| `TB_01_metadata.csv` | same | Available (573 room attributes) |

## Expected outputs

| File | Location | Description |
|------|----------|-------------|
| `nodes.csv` | `04_graph_dataset/` | One row per graph node (13 columns) |
| `edges.csv` | `04_graph_dataset/` | One row per edge (src_id, dst_id, edge_type) |
| `01_geometry_and_graph.png` | `05_visuals/` | Topology.Show render |
| `02_graph_by_type.png` | `05_visuals/` | NetworkX coloured by space_type |
| `03_graph_by_floor.png` | `05_visuals/` | NetworkX coloured by floor_id |
| `04_graph_by_apartment.png` | `05_visuals/` | NetworkX coloured by apartment_id |
| `05_degree_distribution.png` | `05_visuals/` | Degree histogram |

## Run order

```
1. resident_gen Grasshopper script (already run — outputs in shared/assets/resident_gen/)
2. 03_notebook_work/A1_01_DoubleL_Geometry_to_Graph.ipynb
      -> produces: 04_graph_dataset/nodes.csv, 04_graph_dataset/edges.csv
                   05_visuals/01_geometry_and_graph.png
3. 03_notebook_work/A1_02_DoubleL_Graph_Visualisation_and_Export.ipynb
      -> produces: 05_visuals/02-05_*.png
                   05_visuals/assignment1_report_summary.txt
```

Default: `DEMO_FLOOR = 0` (floor 0 only, fast). Set to `None` for all 5 floors.

## Current status

**In progress — notebooks written, not yet run.**

Notebook code is complete. Notebooks have not been executed; no CSV or PNG outputs exist yet.

## Blockers

1. **Hardcoded paths need updating.** Notebooks reference:
   - `EXPORTS_DIR = .../resident_gen/...` — now at `shared/assets/resident_gen/Exports/TB_01/`
   - `ASSIGN_ROOT = .../assignment_01_graph_generation` — now at `assignments/assignment_01_graph_generation/`
   - `OUTPUTS_DIR` writes to `outputs/` — folder renamed to `04_graph_dataset/`
   - `VISUALS_DIR` writes to `05_visuals/` — path root changed
   **Action required:** update path constants in both notebooks before first run.

2. **Door geometry unavailable.** `TB_01_doors.obj` is empty (0 objects).
   `Graph.ByTopology(directApertures=True)` cannot be used.
   Current workaround: shared-face adjacency (`direct=True`).
   **Fix:** regenerate TB_01 export with door geometry from Grasshopper.

3. **Corridor connectors absent.** Stair/lift inter-floor connections not in exports.
   Vertical circulation graph edges not possible with current geometry.

## Folder contents

| Folder | Contents |
|--------|----------|
| `00_brief_and_references/` | OBJ_EXPORTER_USAGE.md; topologicpy_obj_exporter.py (stub) |
| `01_grasshopper_source/` | Empty — Grasshopper source file location |
| `02_rhino_exports/` | Empty — OBJ files exported directly from Rhino go here |
| `03_notebook_work/` | A1_01_DoubleL_Geometry_to_Graph.ipynb; A1_02_DoubleL_Graph_Visualisation_and_Export.ipynb |
| `04_graph_dataset/` | Empty — nodes.csv and edges.csv written here at runtime |
| `05_visuals/` | Empty — PNG figures written here at runtime |
| `06_submission_text/` | Empty — written interpretation goes here |

## Note on BGR notebook

`A1_01_DoubleL_BGR_Graph_Generation.ipynb` (earlier session work) has been moved to
`archive/superseded_work/`. It applies the BGR massing workflow (S06-13A) to the
Double-L building, which is Assignment 3 material. Assignment 1 uses S02 room-level workflow.
