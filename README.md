# GML_Edu — MaCAD S.3: Buildings as Graphs

Student repository for the MaCAD S.3 Graph Machine Learning course.
Rebuilt from first principles; all geometry and code is original work.

## Repository structure

```
/
├── class_notebooks/          Official course notebooks (read-only reference)
│   ├── S02_geometry_to_topology/
│   ├── S03_graph_analysis/
│   ├── S04_ifc_to_graph/
│   ├── S05_graph_datasets/
│   ├── S06_graph_ml/
│   └── S07_graph_generation_neo4j/
│
├── assignments/
│   ├── assignment_01_graph_generation/   Room-and-circulation graph from OBJ geometry
│   ├── assignment_02_graph_analysis/     Graph metric analysis and spatial interpretation
│   └── assignment_03_no_grad_evaluation/ BGR no-grad prediction with pretrained model
│
├── shared/
│   ├── assets/
│   │   ├── resident_gen/            Grasshopper generator exports (TB_01, BB_01)
│   │   └── course_supporting_files/ OBJ, IFC, model files from course
│   ├── scripts/                     Shared utility scripts
│   └── docs/                        Methodology notes, notebook map, planning docs
│
├── final_project/                   Comparative residential layout analysis (not started)
│
└── archive/
    ├── duplicate_notebooks/         Exact or near-duplicate course notebooks
    ├── obsolete_outputs/            Generated files from superseded workflows
    └── superseded_work/             Notebook variants replaced by later work
```

## Assignments

| # | Name | Status | Primary references |
|---|------|--------|--------------------|
| 1 | Graph Generation | In progress | S02 geometry-to-topology notebooks |
| 2 | Graph Analysis | Not started | S03 spatial intelligence notebooks |
| 3 | No-Grad Evaluation | Not started | S06-13A, S06-13B notebooks |

## Key constraint

`shared/assets/resident_gen/` contains exports from the resident_gen Grasshopper generator:
- `TB_01/` — Double-L residential layout (5 floors, 573 rooms) — **Assignment 1 source**
- `BB_01/` — Two-bar layout (2 floors, 81 rooms, 73 doors) — **Final project source**

`TB_01_doors.obj` is empty (0 doors exported). Assignment 1 uses shared-face adjacency
as the edge strategy. Door-access edges require geometry fix in Grasshopper first.

## References

All course notebooks are in `class_notebooks/` organised by session.
Do not modify course notebooks. Do not copy content from external student repositories.
