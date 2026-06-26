# OBJ Exporter — Usage Guide

Script: `topologicpy_obj_exporter.py`  
For use with: Grasshopper Python 3 component, Rhino 8 / CPython

---

## 1. Component inputs

| Name | Type | Access | Description |
|---|---|---|---|
| `Geometry` | Geometry | List | Breps or surfaces to export. For `spaces`, every item must be a closed solid. |
| `Object_Names` | Text | List | One name per geometry item, in the same order. Names drive the `g GroupName` entries in the OBJ and become the `name` key that TopologicPy reads. |
| `Layout_ID` | Text | Item | Short identifier for the layout variant, e.g. `TB_01`, `L_02`. Appears in the output filename and in the OBJ header. |
| `Category` | Text | Item | One of exactly three values: `spaces`, `doors`, `windows`. Controls validation rules and the output filename suffix. |
| `Export_Folder` | Text | Item | Absolute path to the folder where the OBJ file will be written. The folder is created if it does not exist. |
| `Export` | Boolean | Item | Nothing happens while this is `False`. Set to `True` only when inputs are ready. |
| `Mesh_Density` | Text | Item | `simple` (fast, coarse — default), `medium` (balanced), or `detailed` (fine). TopologicPy only needs faces and adjacency; `simple` is sufficient for Assignment 1. |
| `Overwrite` | Boolean | Item | `False` by default. Set to `True` to replace an existing OBJ file. The exporter will not silently overwrite. |

---

## 2. Component outputs

| Name | Type | Description |
|---|---|---|
| `OBJ_Path` | Text | Full absolute path of the written file, or empty if export did not complete. |
| `Status` | Text | One-line result: `OK`, `Partial`, `Blocked`, `Failed`, or `Idle`. |
| `Export_Count` | Integer | Number of objects successfully written. Zero if export did not run. |
| `Failed_Objects` | Text (List) | One entry per rejected geometry item. Each entry names the object and states the rejection reason. Empty on full success. |
| `Report` | Text | Full multi-line export log. Inspect this first when anything is unexpected. |

---

## 3. Required naming convention

### Layout_ID

Use the format `TypeCode_Index`:

| Code | Meaning |
|---|---|
| `TB` | Two-bar layout |
| `L` | L-shaped layout |

Examples: `TB_01`, `TB_02`, `TB_03`, `L_01`, `L_02`, `L_03`

`Layout_ID` must contain only letters, digits, underscores, and hyphens. No spaces.

### Object_Names

Each space, door, or window needs a unique name within its export. Allowed characters: `A–Z a–z 0–9 _ -`

Recommended convention for spaces:

```
Bar_A_Living_01
Bar_A_Bed_01
Bar_A_Bath_01
Bar_B_Living_01
Bar_B_Bed_01
```

For doors and windows, a simple `Door_01`, `Win_01` numbering is sufficient since TopologicPy identifies them geometrically, not by name.

**Duplicate names within one export are rejected.** The same name may appear in different categories (a `Door_01` in `doors` and a `Door_01` in `windows`) since they go into separate files.

---

## 4. Output files per layout

Run the component three times — once per category — to produce the three files that the Assignment 1 notebook expects:

```
TB_01_spaces.obj
TB_01_doors.obj
TB_01_windows.obj
```

Change `Layout_ID` to `TB_02`, `TB_03`, `L_01`, etc. to produce the full set for comparative analysis:

```
TB_01_spaces.obj    TB_02_spaces.obj    TB_03_spaces.obj
L_01_spaces.obj     L_02_spaces.obj     L_03_spaces.obj
```

Keep all OBJ files for one layout in the same folder so the notebook can reference them with one base path.

---

## 5. First test: TB_01_spaces only

Before exporting doors and windows, verify the spaces export works end-to-end.

**In Grasshopper:**
1. Connect your room Breps to `Geometry` (List access).
2. Connect a matching list of names to `Object_Names`.
3. Set `Layout_ID` = `TB_01`.
4. Set `Category` = `spaces`.
5. Set `Export_Folder` to the absolute path of `assignment_01_graph_generation/assets/`.
6. Set `Mesh_Density` = `simple`.
7. Set `Overwrite` = `False`.
8. Set `Export` = `False` first; check that `Status` reads `Idle`.
9. Flip `Export` to `True`.

**Expected outputs if geometry is valid:**
- `Status`: `OK — N/N objects exported to TB_01_spaces.obj.`
- `OBJ_Path`: full path ending in `TB_01_spaces.obj`
- `Export_Count`: equals your room count
- `Failed_Objects`: empty
- `Report`: lists each accepted room

**Open the OBJ in a text editor and check:**
- First line: `# TopologicPy OBJ Export`
- Each room appears as a `g RoomName` block
- Number of `g` lines equals your room count
- `f` lines exist inside every group (missing `f` lines mean the Brep was not a closed solid)

**In Python (no Rhino needed), count groups:**
```python
with open("TB_01_spaces.obj") as f:
    lines = f.readlines()
groups = [l for l in lines if l.startswith("g ")]
faces  = [l for l in lines if l.startswith("f ")]
print("Groups:", len(groups), "  Faces:", len(faces))
```

Once `TB_01_spaces.obj` loads correctly in the TopologicPy notebook, proceed to export doors and windows.

---

## 6. Why spaces must be closed solids

TopologicPy builds its `CellComplex` by treating each imported geometry object as a closed volumetric cell. The function `Cell.ByFaces(faces)` requires a complete, watertight face set — every edge must be shared by exactly two faces with no gaps.

If a room Brep has any open boundary (naked edges), `Cell.ByFaces()` returns `None`. That room silently drops out of the `CellComplex`, produces no graph node, and shares no edges with its neighbours. The resulting graph is wrong without any error being raised by TopologicPy.

The exporter checks `brep.IsSolid` and rejects any room that is not a closed solid. It does not attempt repair. The rejection message names the room and directs you to Rhino's `ShowEdges > Naked Edges` command.

**Fix in Rhino, not in the exporter.** Common causes:

- Room outline was not fully closed before extrusion.
- `Cap` was not applied to an open extrusion.
- Boolean operation left a gap.
- Two room volumes do not meet exactly (sub-millimetre gap at the shared wall).

---

## 7. Why doors and windows should be exported separately

Doors and windows are apertures, not cells. TopologicPy processes them differently from room volumes:

```python
# Spaces → CellComplex (rooms with adjacency)
cc = CellComplex.ByCells(room_cells)

# Apertures → added to the CellComplex after it is built
cc_with_apertures = Topology.AddApertures(cc, aperture_faces)

# Graph through apertures (doors and windows control which rooms connect)
graph = Graph.ByTopology(
    cc_with_apertures,
    direct              = True,
    viaSharedApertures  = True,
    toExteriorApertures = True
)
```

Separating them into two files (`_doors.obj`, `_windows.obj`) lets you:

1. Load each aperture type independently and assign different visual styles and attributes.
2. Build separate graph variants — for example, a circulation graph using only doors (`toExteriorApertures = False`) vs. a light-access graph using only windows (`toExteriorApertures = True`).
3. Debug aperture placement without re-exporting room geometry.

Export doors and windows **after** `TB_01_spaces.obj` has been verified in the notebook. Aperture geometry that misses the wall plane by even a small tolerance will not register as an aperture in TopologicPy.
