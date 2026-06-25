# Final Project — Comparative Residential Layouts

## Purpose

Compare two residential layout typologies — two parallel bars and two L-shaped blocks — using graph machine learning. The analysis applies node classification (room type prediction) and graph metric comparison to evaluate how spatial organisation differs between typologies.

## Expected inputs

- Rhino models for both typologies exported as OBJ files.
- Node feature dataset derived from each typology via TopologicPy.
- Pretrained or trained node classification model (following S06-15 workflow).

## Expected outputs

- `datasets/` — graph CSV datasets for both typologies (nodes.csv, edges.csv, graphs.csv, meta.yaml).
- `outputs/` — node classification predictions; comparative metric tables.
- `visuals/` — graph plots, metric comparison charts, spatial diagrams.
- `presentation/` — slide deck or equivalent communicating methodology and findings.
- `docs/` — written interpretation of typological differences as revealed by graph analysis.

## Folder contents

| Folder | Contents |
|---|---|
| `assets/` | OBJ files for both typologies |
| `datasets/` | Graph feature datasets |
| `notebooks/` | Graph construction, feature engineering, classification notebooks |
| `outputs/` | Model predictions and metric results |
| `visuals/` | Charts, graph plots, spatial diagrams |
| `presentation/` | Final presentation files |
| `docs/` | Methodology and interpretation notes |

## Typologies

- **Two bars** — two rectangular residential blocks arranged in parallel.
- **Two L-shaped blocks** — two L-shaped residential blocks.

The comparison investigates whether graph structure (topology, metrics, predicted room types) reflects the spatial and programmatic differences between these two layout strategies.

## Current status

**Not started.**
