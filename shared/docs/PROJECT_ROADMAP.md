# Project Roadmap

## Assignment 1 — Graph Generation

**Pipeline:** Rhino model → OBJ export → TopologicPy → graph object → CSV output

Steps:
1. Model architectural floor plan in Rhino.
2. Export geometry as OBJ file(s).
3. Import OBJ into TopologicPy; construct CellComplex.
4. Extract adjacency graph from CellComplex.
5. Export nodes and edges as CSV.

Key notebooks: S02-06 (OBJ import), S03-07/08/09 (spatial intelligence).

---

## Assignment 2 — Graph Analysis

**Pipeline:** Graph CSV → metric computation → spatial interpretation → comparison

Steps:
1. Load graph CSV from Assignment 1.
2. Compute graph metrics (degree, betweenness, clustering, diameter, etc.).
3. Map metrics to spatial meaning (circulation, connectivity, accessibility).
4. Compare results across layout variants or against reference graphs.

Key notebooks: S03-07/08/09.

---

## Assignment 3 — BGR Evaluation

**Pipeline:** Rhino BGR model → four OBJ files → 13A graph creation → 13B no-grad prediction

Steps:
1. Produce a Bedroom / Guest room / Reception (BGR) model in Rhino.
2. Export four OBJ files (one per spatial layer or variant).
3. **13A** — load OBJ files, build graph features, assemble dataset.
4. **13B** — load pretrained `bgr_model.pt`, run inference with `torch.no_grad()`, record predicted room-type labels.

Key notebooks: S06-13A (graph creation, student version), S06-13B (no-grad prediction).

---

## Final Project — Comparative Residential Layouts

**Typologies compared:** Two parallel bars vs two L-shaped blocks.

Pipeline:
1. Model both typologies in Rhino.
2. Export each as OBJ; build graphs via TopologicPy.
3. Engineer node and graph features.
4. Run node classification (room type) using S06-15 workflow.
5. Compare graph metrics and model predictions across typologies.
6. Produce presentation showing spatial interpretation of results.

Key notebooks: S06-13A, S06-15 (node classification).
