# GML_Edu — MaCAD S.3: Buildings as Graphs

Student repository for the MaCAD S.3 Graph Machine Learning course.
Applies the Two-Bars resident_gen geometry and the course BGR workflow to an original Rhino pilotis model.

## Repository structure

```
/
├── class_notebooks/
│   ├── S02_geometry_to_topology/   S02-01 through S02-06
│   ├── S03_graph_analysis/         S03-07 through S03-09
│   ├── S04_ifc_to_graph/           S04-10A, S04-10A expanded, S04-11B
│   ├── S05_graph_datasets/         S05-12
│   ├── S06_graph_ml/               S06-13, 13A, 13B, 14, 15
│   └── S07_graph_generation_neo4j/ S07-16 through S07-20
│
├── assignments/
│   ├── assignment_01_graph_generation/   Room-and-circulation graph from OBJ geometry
│   ├── assignment_02_graph_analysis/     Graph metric analysis and spatial interpretation
│   └── assignment_03_no_grad_evaluation/ BGR no-grad prediction with pretrained model
│
├── shared/
│   ├── assets/
│   │   ├── resident_gen/Exports/    Grasshopper generator exports (BB_01, BB_02, BB_03)
│   │   └── course_supporting_files/ bgr_model.pt, OBJ, IFC, course datasets
│   ├── scripts/                     Shared utility scripts
│   └── docs/                        Notebook map, planning docs, requirements checklist
│
├── final_project/                   Comparative residential layout analysis (pending)
│
└── archive/
    ├── duplicate_notebooks/         Near-duplicate course notebooks
    ├── obsolete_outputs/            Generated files from superseded workflows
    └── superseded_work/             Notebook variants replaced by later work
```

## Assignments

| # | Name | Status | Key outputs |
|---|------|--------|-------------|
| 1 | Graph Generation | **Complete** | BB_01/02/03 nodes.csv + edges.csv; 9 visuals per building |
| 2 | Graph Analysis | **Mostly complete** | BB_01/02/03 metrics CSVs; full visuals and interpretation for BB_01 only |
| 3 | No-Grad Evaluation | **Complete** | BGR graph dataset; model pred_label=1 (Separation with Plinth, prob≈0.9999) |

## Source geometry

`shared/assets/resident_gen/Exports/` contains exports from the Two-Bars resident_gen Grasshopper generator:

| Folder | Description | Nodes | Edges |
|--------|-------------|-------|-------|
| `BB_01/` | Two-bars, standard layout | 175 | 388 |
| `BB_02/` | Two-bars, deeper plan | 381 | 858 |
| `BB_03/` | Two-bars, wider apartments | 141 | 303 |

Assignment 1 uses bounding-box spatial adjacency (0.45 m gap tolerance) because door geometry
is absent from the resident_gen OBJ exports.

## Assignment 3 BGR result

Model prediction: **Separation with Plinth** (label 1), probability ≈ 0.9999.
Student manual label recorded in `graphs.csv`: **Separation** (label 0).
The model prediction and the student's manual typological assessment differ.

Pretrained model: `shared/assets/course_supporting_files/bgr_model.pt` (34.8 MB, not retrained).

## References

All course notebooks are in `class_notebooks/` organised by session. Do not modify them.
Planning documents and the requirements checklist are in `shared/docs/`.
