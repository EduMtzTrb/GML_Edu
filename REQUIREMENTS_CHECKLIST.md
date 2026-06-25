# Requirements Checklist

## Confirmed minimum course requirements

These are explicitly stated in course materials.

- [ ] Assignment 1: Submit graph CSV (nodes + edges) derived from a Rhino model via TopologicPy.
- [ ] Assignment 2: Submit graph metric analysis with spatial interpretation commentary.
- [ ] Assignment 3 (13A): Submit graph creation notebook with own four OBJ files loaded correctly.
- [ ] Assignment 3 (13B): Submit no-gradient prediction notebook; show predicted BGR labels for own model.
- [ ] Final project: Submit comparative analysis of two residential layout typologies using graph ML.
- [ ] Final project: Include presentation (slides or equivalent) communicating results.

---

## Course-workflow requirements inferred from student examples

These patterns appear consistently in reference student repositories but are not stated verbatim in course documents.

- [ ] OBJ files organised by spatial layer (ground, columns, core, offices or equivalent).
- [ ] Graph CSV follows the shared schema: `nodes.csv` with feature columns, `edges.csv` with `source`/`target`.
- [ ] `meta.yaml` accompanies each dataset folder.
- [ ] Pretrained model file (`bgr_model.pt`) used as-is without retraining.
- [ ] Node features in Assignment 3 match the feature set expected by `bgr_model.pt`.
- [ ] Final project dataset follows the same CSV/YAML schema as the classification dataset.
- [ ] Visualisations (graph plots, metric charts) included in notebooks before export.

---

## Portfolio enhancements

Optional additions that go beyond minimum requirements.

- [ ] Annotated visuals comparing the two final-project typologies side by side.
- [ ] Concise written interpretation of what each graph metric reveals spatially.
- [ ] Clean, well-commented notebooks suitable for public portfolio display.
- [ ] Presentation deck with rendered plan diagrams and graph overlays.
- [ ] `docs/` folder in each assignment with a short methodology note.
