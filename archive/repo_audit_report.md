# Repository Audit Report

**Date:** 2026-06-26  
**Scope:** MaCAD S.3 — Buildings as Graphs (GML_Edu)  
**Auditor:** Claude Code (structural reorganisation only — no notebook code modified)

---

## 1. Original Problems Found

| # | Problem | Severity |
|---|---------|----------|
| 1 | All assignments were at the repository root, not under `assignments/` | High |
| 2 | Course notebooks were under `references/Graph ML -- NOTEBOOKS/` with no session grouping | High |
| 3 | Assignment 3 was named `assignment_03_bgr_evaluation` — incorrect per course name | Medium |
| 4 | Assignment 01 had duplicate/conflicting folder names: `notebooks/` vs `03_notebook_work/`, `visuals/` vs `05_visuals/`, `outputs/` vs `04_graph_dataset/` (not yet created) | Medium |
| 5 | `A1_01_DoubleL_BGR_Graph_Generation.ipynb` (BGR/S06-13A workflow) was inside Assignment 1; it is Assignment 3 material | High |
| 6 | `resident_gen/` was at the repository root; it is shared data used by Assignment 1 and the final project | Medium |
| 7 | `PROJECT_ROADMAP.md` and `REQUIREMENTS_CHECKLIST.md` were at root; they are planning docs | Low |
| 8 | `references/course_workflow/` and `references/student_repo_comparison/` had no clear home | Low |
| 9 | Duplicate S06-14 notebook: `S06-14 GML Graph Regression.ipynb` and `S06-14 GML Regression.ipynb` (same session number, shorter name is subset/draft) | Medium |
| 10 | Two S07-18 notebooks with different titles; two "S07-19 GraphRAG Part 1" and "S07-18 GraphRAG Part 1" may be duplicates | Low |
| 11 | Assignment 01 `docs/OBJ_EXPORTER_USAGE.md` and `docs/topologicpy_obj_exporter.py` were deleted during restructure (were untracked files — see §4) | High |
| 12 | Assignment 01 notebooks have hardcoded paths that no longer match the new structure | Medium |

---

## 2. Files Moved

### Course notebooks → class_notebooks/

| From | To |
|------|----|
| `references/Graph ML -- NOTEBOOKS/S02-01 Primal vs Dual.ipynb` | `class_notebooks/S02_geometry_to_topology/` |
| `references/Graph ML -- NOTEBOOKS/S02-02 Metric vs Topological.ipynb` | `class_notebooks/S02_geometry_to_topology/` |
| `references/Graph ML -- NOTEBOOKS/S02-03 Adjacency Vs Access.ipynb` | `class_notebooks/S02_geometry_to_topology/` |
| `references/Graph ML -- NOTEBOOKS/S02-04 Geometric Representations.ipynb` | `class_notebooks/S02_geometry_to_topology/` |
| `references/Graph ML -- NOTEBOOKS/S02-05 Spatial Representations.ipynb` | `class_notebooks/S02_geometry_to_topology/` |
| `references/Graph ML -- NOTEBOOKS/S02-06 Importing OBJ files.ipynb` | `class_notebooks/S02_geometry_to_topology/` |
| `references/Graph ML -- NOTEBOOKS/S03-07 Spatial Intelligence Part 1.ipynb` | `class_notebooks/S03_graph_analysis/` |
| `references/Graph ML -- NOTEBOOKS/S03-08 Spatial Intelligence Part 2.ipynb` | `class_notebooks/S03_graph_analysis/` |
| `references/Graph ML -- NOTEBOOKS/S03-09 Spatial Intelligence Part 3.ipynb` | `class_notebooks/S03_graph_analysis/` |
| `references/Graph ML -- NOTEBOOKS/S04-10 A. IFC Semantic Relationships.ipynb` | `class_notebooks/S04_ifc_to_graph/` |
| `references/Graph ML -- NOTEBOOKS/S04-10_A_IFC_Semantic_Relationships_GQL_Expanded.ipynb` | `class_notebooks/S04_ifc_to_graph/` |
| `references/Graph ML -- NOTEBOOKS/S04-11 B. IFC Spatial Relationships.ipynb` | `class_notebooks/S04_ifc_to_graph/` |
| `references/Graph ML -- NOTEBOOKS/S05-12 Dataset and Feature Engineering.ipynb` | `class_notebooks/S05_graph_datasets/` |
| `references/Graph ML -- NOTEBOOKS/S06-13 GML Graph Classification.ipynb` | `class_notebooks/S06_graph_ml/` |
| `references/Graph ML -- NOTEBOOKS/S06-13A GML Creating BGR Graph - STUDENT.ipynb` | `class_notebooks/S06_graph_ml/` |
| `references/Graph ML -- NOTEBOOKS/S06-13B GML Predict BGR Graph.ipynb` | `class_notebooks/S06_graph_ml/` |
| `references/Graph ML -- NOTEBOOKS/S06-14 GML Graph Regression.ipynb` | `class_notebooks/S06_graph_ml/` |
| `references/Graph ML -- NOTEBOOKS/S06-15 GML Node Classification.ipynb` | `class_notebooks/S06_graph_ml/` |
| `references/Graph ML -- NOTEBOOKS/S07-16 Neo4j Installation.ipynb` | `class_notebooks/S07_graph_generation_neo4j/` |
| `references/Graph ML -- NOTEBOOKS/S07-17 Ollama_installation.ipynb` | `class_notebooks/S07_graph_generation_neo4j/` |
| `references/Graph ML -- NOTEBOOKS/S07-18 GraphRAG Part 1.ipynb` | `class_notebooks/S07_graph_generation_neo4j/` |
| `references/Graph ML -- NOTEBOOKS/S07-18 Neo4j Tutorial.ipynb` | `class_notebooks/S07_graph_generation_neo4j/` |
| `references/Graph ML -- NOTEBOOKS/S07-19 GraphRAG Part 1.ipynb` | `class_notebooks/S07_graph_generation_neo4j/` |
| `references/Graph ML -- NOTEBOOKS/S07-20 GraphRAG Part 2.ipynb` | `class_notebooks/S07_graph_generation_neo4j/` |

### Course supporting files → shared/assets/

| From | To |
|------|----|
| `references/Graph ML -- NOTEBOOKS/Supporting Files/` | `shared/assets/course_supporting_files/` |

### Reference docs → shared/docs/

| From | To |
|------|----|
| `references/course_workflow/` | `shared/docs/course_workflow/` |
| `references/student_repo_comparison/` | `shared/docs/student_repo_comparison/` |
| `PROJECT_ROADMAP.md` | `shared/docs/PROJECT_ROADMAP.md` |
| `REQUIREMENTS_CHECKLIST.md` | `shared/docs/REQUIREMENTS_CHECKLIST.md` |

### Assignments → assignments/

| From | To |
|------|----|
| `assignment_01_graph_generation/` | `assignments/assignment_01_graph_generation/` |
| `assignment_02_graph_analysis/` | `assignments/assignment_02_graph_analysis/` |
| `assignment_03_bgr_evaluation/` | `assignments/assignment_03_no_grad_evaluation/` (renamed) |

### Shared data → shared/assets/

| From | To |
|------|----|
| `resident_gen/` | `shared/assets/resident_gen/` |

### Assignment 01 internal restructure

Old folder | New folder
-----------|-----------
`assignment_01_graph_generation/docs/` | `00_brief_and_references/` (contents moved)
`assignment_01_graph_generation/assets/` | `02_rhino_exports/` (placeholder only — contents were empty)
`assignment_01_graph_generation/outputs/` | `04_graph_dataset/` (placeholder — contents empty)
`assignment_01_graph_generation/notebooks/` | removed (replaced by `03_notebook_work/`)
`assignment_01_graph_generation/visuals/` | removed (replaced by `05_visuals/`)

New folders created: `00_brief_and_references/`, `01_grasshopper_source/`, `02_rhino_exports/`, `04_graph_dataset/`, `06_submission_text/`

---

## 3. Files Archived

| File | Archived to | Reason |
|------|-------------|--------|
| `assignment_01_graph_generation/03_notebook_work/A1_01_DoubleL_BGR_Graph_Generation.ipynb` | `archive/superseded_work/` | BGR massing workflow (S06-13A) applied to Assignment 1 Double-L building. This is Assignment 3 material. Superseded by room-level S02 workflow in `A1_01_DoubleL_Geometry_to_Graph.ipynb`. Retained as methodology reference for Assignment 3. |
| `references/Graph ML -- NOTEBOOKS/S06-14 GML Regression.ipynb` | `archive/duplicate_notebooks/` | Duplicate of `S06-14 GML Graph Regression.ipynb`. Shorter title suggests an earlier or draft version. Canonical copy retained in `class_notebooks/S06_graph_ml/`. |

---

## 4. Files Deleted

| File | Why deleted | Recovery |
|------|------------|----------|
| `assignment_01_graph_generation/docs/OBJ_EXPORTER_USAGE.md` | Untracked file. Deleted during restructure when `docs/` was removed with `-Recurse`. | **Recreated** from memory at `assignments/assignment_01_graph_generation/00_brief_and_references/OBJ_EXPORTER_USAGE.md` — full content recovered. |
| `assignment_01_graph_generation/docs/topologicpy_obj_exporter.py` | Untracked file. Deleted with same operation. | **Recreated stub** at `assignments/assignment_01_graph_generation/00_brief_and_references/topologicpy_obj_exporter.py`. Only the 30-line header was in context; full body needs reconstruction from Grasshopper component history or from the specification in `OBJ_EXPORTER_USAGE.md`. |
| `references/Graph ML -- NOTEBOOKS/` (empty folder) | Removed after all contents moved to `class_notebooks/` | N/A |
| `references/` (empty folder) | Removed after all contents moved | N/A |
| Empty `.gitkeep`-only folders in assignments 01/02/03 | All were placeholder folders replaced by numbered counterparts | N/A |

---

## 5. Duplicate or Incorrect Notebooks Found

### Confirmed duplicate
- `S06-14 GML Graph Regression.ipynb` vs `S06-14 GML Regression.ipynb`
  - Same session number, shorter name is likely a draft
  - Canonical: `class_notebooks/S06_graph_ml/S06-14 GML Graph Regression.ipynb`
  - Archived: `archive/duplicate_notebooks/S06-14 GML Regression.ipynb`

### Potential duplicates (not archived — content not compared)
- `S07-18 GraphRAG Part 1.ipynb` AND `S07-19 GraphRAG Part 1.ipynb` share the same title
  - Both kept in `class_notebooks/S07_graph_generation_neo4j/` pending content comparison
  - One may be an earlier draft of the other

### Misplaced notebook (now corrected)
- `A1_01_DoubleL_BGR_Graph_Generation.ipynb` was in `assignment_01_graph_generation/03_notebook_work/`
  - Applies S06-13A BGR workflow — this is Assignment 3 material
  - Moved to `archive/superseded_work/`

---

## 6. Final Notebook-to-Assignment Mapping

### Assignment 1 — Graph Generation

| Notebook | Location | Role | Status |
|----------|----------|------|--------|
| `A1_01_DoubleL_Geometry_to_Graph.ipynb` | `assignments/assignment_01_graph_generation/03_notebook_work/` | Primary — geometry to graph | Written, not yet run |
| `A1_02_DoubleL_Graph_Visualisation_and_Export.ipynb` | same | Primary — visualisation | Written, not yet run |

Primary references: `class_notebooks/S02_geometry_to_topology/S02-01` through `S02-06`

### Assignment 2 — Graph Analysis

| Notebook | Location | Role | Status |
|----------|----------|------|--------|
| *(none yet)* | `assignments/assignment_02_graph_analysis/02_notebook_work/` | To be written | Not started |

Primary references: `class_notebooks/S03_graph_analysis/S03-07` through `S03-09`

### Assignment 3 — No-Grad Evaluation

| Notebook | Location | Role | Status |
|----------|----------|------|--------|
| *(none yet)* | `assignments/assignment_03_no_grad_evaluation/02_notebook_work/` | Adapt S06-13A + 13B | Not started |

Primary references: `class_notebooks/S06_graph_ml/S06-13A`, `S06-13B`

---

## 7. Remaining Blockers for Assignment 1

### Blocker 1 — Hardcoded paths (IMMEDIATE — must fix before first run)

Both Assignment 1 notebooks contain hardcoded paths that are now wrong:

```python
# Current (wrong after reorganisation):
PROJECT_ROOT = "D:/GitHub/GML_Edu"
EXPORTS_DIR  = os.path.join(PROJECT_ROOT, "resident_gen", "Exports", "TB_01")
ASSIGN_ROOT  = os.path.join(PROJECT_ROOT, "assignment_01_graph_generation")
OUTPUTS_DIR  = os.path.join(ASSIGN_ROOT, "outputs")
VISUALS_DIR  = os.path.join(ASSIGN_ROOT, "05_visuals")

# Correct after reorganisation:
PROJECT_ROOT = "D:/GitHub/GML_Edu"
EXPORTS_DIR  = os.path.join(PROJECT_ROOT, "shared", "assets", "resident_gen", "Exports", "TB_01")
ASSIGN_ROOT  = os.path.join(PROJECT_ROOT, "assignments", "assignment_01_graph_generation")
OUTPUTS_DIR  = os.path.join(ASSIGN_ROOT, "04_graph_dataset")
VISUALS_DIR  = os.path.join(ASSIGN_ROOT, "05_visuals")
```

### Blocker 2 — Door geometry empty

`shared/assets/resident_gen/Exports/TB_01/TB_01_doors.obj` contains 0 objects.
`Graph.ByTopology(directApertures=True)` cannot be used. Current workaround
(shared-face adjacency, `direct=True`) is documented in both notebooks.
Fix requires regenerating the TB_01 export with door geometry from Grasshopper.

### Blocker 3 — Corridor connectors absent

No stair or lift connector geometry in TB_01 exports. Vertical inter-floor
circulation edges cannot be encoded. Not a blocker for running the notebooks
(they handle it gracefully), but is a graph quality limitation.

### Blocker 4 — topologicpy_obj_exporter.py body missing

The Python body of the Grasshopper OBJ exporter script was lost during restructure
(§4). The stub at `00_brief_and_references/topologicpy_obj_exporter.py` contains
the header and specification only. The full implementation needs to be recovered
from Grasshopper component history.

---

## 8. Final Repository Tree

```
D:\GitHub\GML_Edu\
├── README.md
│
├── class_notebooks\
│   ├── S02_geometry_to_topology\          (6 notebooks: S02-01 through S02-06)
│   ├── S03_graph_analysis\                (3 notebooks: S03-07 through S03-09)
│   ├── S04_ifc_to_graph\                  (3 notebooks: S04-10A, S04-10A expanded, S04-11B)
│   ├── S05_graph_datasets\                (1 notebook: S05-12)
│   ├── S06_graph_ml\                      (5 notebooks: S06-13, 13A, 13B, 14, 15)
│   └── S07_graph_generation_neo4j\        (6 notebooks: S07-16 through S07-20)
│
├── assignments\
│   ├── assignment_01_graph_generation\
│   │   ├── 00_brief_and_references\       OBJ_EXPORTER_USAGE.md, topologicpy_obj_exporter.py (stub)
│   │   ├── 01_grasshopper_source\         (empty — .gitkeep)
│   │   ├── 02_rhino_exports\              (empty — .gitkeep)
│   │   ├── 03_notebook_work\              A1_01_DoubleL_Geometry_to_Graph.ipynb
│   │   │                                  A1_02_DoubleL_Graph_Visualisation_and_Export.ipynb
│   │   ├── 04_graph_dataset\              (empty — .gitkeep; nodes.csv + edges.csv written here at run time)
│   │   ├── 05_visuals\                    (empty; PNGs written here at run time)
│   │   ├── 06_submission_text\            (empty — .gitkeep)
│   │   └── README.md
│   │
│   ├── assignment_02_graph_analysis\
│   │   ├── 00_brief_and_references\
│   │   ├── 01_input_graph\
│   │   ├── 02_notebook_work\
│   │   ├── 03_results\
│   │   ├── 04_visuals\
│   │   ├── 05_submission_text\
│   │   └── README.md
│   │
│   └── assignment_03_no_grad_evaluation\
│       ├── 00_brief_and_references\
│       ├── 01_input_graph\
│       ├── 02_notebook_work\
│       ├── 03_predictions\
│       ├── 04_visuals\
│       ├── 05_submission_text\
│       └── README.md
│
├── shared\
│   ├── assets\
│   │   ├── resident_gen\Exports\
│   │   │   ├── TB_01\                     TB_01_rooms.obj, corridors.obj, cores.obj, doors.obj (empty),
│   │   │   │                              metadata.csv, manifest.json, export_report.txt
│   │   │   └── BB_01\                     BB_01_rooms.obj, corridors.obj, cores.obj, doors.obj (73 doors),
│   │   │                                  windows.obj, metadata.csv, manifest.json, export_report.txt
│   │   └── course_supporting_files\       bgr_model.pt, ground/columns/offices/core OBJ+MTL,
│   │                                      IFC files, gallery.brep, Rhino_Geometry.obj, PDF,
│   │                                      dataset_graph_classification/, dataset_graph_regression/,
│   │                                      dataset_node_classification/, dataset_graphRAG/
│   ├── scripts\                           (empty — .gitkeep)
│   └── docs\
│       ├── PROJECT_ROADMAP.md
│       ├── REQUIREMENTS_CHECKLIST.md
│       ├── course_workflow\NOTEBOOK_MAP.md
│       └── student_repo_comparison\README.md
│
├── final_project\                         Not started. Internal structure unchanged.
│   (assets, datasets, docs, notebooks, outputs, presentation, visuals — all .gitkeep)
│   └── README.md
│
└── archive\
    ├── duplicate_notebooks\
    │   └── S06-14 GML Regression.ipynb   (duplicate of S06-14 GML Graph Regression.ipynb)
    ├── obsolete_outputs\                  (empty)
    └── superseded_work\
        └── A1_01_DoubleL_BGR_Graph_Generation.ipynb  (Assignment 3 material, not Assignment 1)
```

---

## Items Not Changed (Ambiguous or Out of Scope)

| Item | Reason not changed |
|------|-------------------|
| `final_project/` | Not in target structure but is legitimate course work; not archived since it has a clear README and is not abandoned. Left at root level. |
| `class_notebooks/S07_graph_generation_neo4j/S07-18 GraphRAG Part 1.ipynb` vs `S07-19 GraphRAG Part 1.ipynb` | Same title on different numbers — content not compared. Both retained pending manual review. |
| Assignment 01 notebook code | Hardcoded paths are wrong after reorganisation but instructions said not to modify code in this task. |

---

## Assignment 1 Structural Readiness

**Structurally ready to continue.** The two S02-based notebooks are in place at
`assignments/assignment_01_graph_generation/03_notebook_work/`. The geometry data
is at `shared/assets/resident_gen/Exports/TB_01/`.

**Immediate next step before running:**
Update the four path constants in both notebooks (see Blocker 1 above).
Then run `A1_01` and confirm it produces `04_graph_dataset/nodes.csv` and `edges.csv`
before running `A1_02`.
