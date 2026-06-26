"""
TopologicPy OBJ Exporter
========================
Grasshopper Python 3 Component Script  |  Rhino 8 / CPython

Exports named Grasshopper geometry to OBJ files formatted for the
TopologicPy Assignment 1 workflow.  One file is produced per run:
    <Layout_ID>_<category>.obj   e.g.  TB_01_spaces.obj

Axis convention matches the course Rhino export guide:
    Rhino X  ->  OBJ X   (unchanged)
    Rhino Z  ->  OBJ Y   (height)
    Rhino Y  ->  OBJ -Z  (depth, negated)

Version : 1.0

NOTE: This file was reconstructed from the usage guide header after the
original was lost during a repository reorganisation on 2026-06-26.
The full implementation body needs to be recovered from Grasshopper
component history or rewritten from the usage guide specification.
See OBJ_EXPORTER_USAGE.md for full parameter and behavioural specification.
"""

# ============================================================
# COMPONENT SETUP  — read before pasting into Grasshopper
# ============================================================
#
# OPTION A  GhPython component (legacy, still available in Rhino 8)
#   Right-click the component -> Edit -> add inputs / outputs below.
#
# OPTION B  New Script component (Rhino 8 Script Editor)
#   Open the Script Editor, create a Python 3 script component,
#   add the same parameter names in the Parameters panel.
#
# INPUTS  (set via component parameter panel)
#   Geometry      — Brep list  (List access)
#   Object_Names  — str list   (List access)
#   Layout_ID     — str        (Item access)
#   Category      — str        (Item access)  "spaces" | "doors" | "windows"
#   Export_Folder — str        (Item access)
#   Export        — bool       (Item access)
#   Mesh_Density  — str        (Item access)  "simple" | "medium" | "detailed"
#   Overwrite     — bool       (Item access)
#
# OUTPUTS
#   OBJ_Path      — str
#   Status        — str
#   Export_Count  — int
#   Failed_Objects — str list
#   Report        — str
#
# ============================================================
# IMPLEMENTATION — reconstruct or recover from GH component
# ============================================================
#
# The body of this script was lost during a repository reorganisation.
# Reconstruct using the specification in OBJ_EXPORTER_USAGE.md:
#
# 1. Validate inputs (Export == True, Category in allowed values, etc.)
# 2. Build output filename: f"{Layout_ID}_{Category}.obj"
# 3. Guard against overwrite if Overwrite == False
# 4. For each Brep in Geometry:
#    a. Check brep.IsSolid — reject if False, log to Failed_Objects
#    b. Mesh at requested density
#    c. Write "g {Object_Names[i]}" block to OBJ
#    d. Write v, vn, f lines for all mesh faces
# 5. Prepend OBJ header: "# TopologicPy OBJ Export", Layout_ID, timestamp
# 6. Write file atomically (write to temp, rename on success)
# 7. Set Status, Export_Count, OBJ_Path, Report outputs

raise NotImplementedError(
    "topologicpy_obj_exporter.py body needs to be reconstructed. "
    "See OBJ_EXPORTER_USAGE.md for the full specification."
)
