"""
make_synthetic_elr.py — build a FAKE IRI ELR data.nc with the exact structure
the real download will have, so NB3 Cells 3-6 can be validated before the
licence clears. Numbers are GARBAGE by design; only the STRUCTURE is real.

Structure mirrored from task_B3_tracker.md Section G:
  prob[X Y C | L F], percent
  C unordered, string ids: Below_Normal / Normal / Above_Normal  (select by NAME)
  X 92->155 (1 deg), Y -20->25 (1 deg), L 1..4 months, F one issuance point
  plus target_season[F L]

DRY-RUN SENTINEL: every prob triple sums to 100 exactly, so a NaN/GRID check
that passes here proves the check works; and Below_Normal is deliberately made
the dominant tercile inside the Maritime box so the figure's hatching has
something to render. NONE of these numbers may enter the article.
"""
import numpy as np
from netCDF4 import Dataset, stringtochar

OUT = "data_SYNTHETIC.nc"   # deliberately NOT data.nc — cannot be mistaken for real

# --- axes (must match Section G exactly) ---
X = np.arange(92, 156, 1, dtype="float32")      # 92..155 inclusive
Y = np.arange(-20, 26, 1, dtype="float32")      # -20..25 inclusive
L = np.arange(1, 5, 1, dtype="float32")         # 1..4 months
F = np.array([738.0], dtype="float32")          # one issuance point (value arbitrary)
C_ids = ["Below_Normal", "Normal", "Above_Normal"]

nx, ny, nc_, nl, nf = len(X), len(Y), len(C_ids), len(L), len(F)

rng = np.random.default_rng(0)

# prob[F, L, C, Y, X] in percent, three terciles summing to 100 per cell
prob = np.empty((nf, nl, nc_, ny, nx), dtype="float32")
for fi in range(nf):
    for li in range(nl):
        base = rng.uniform(20, 45, size=(ny, nx))          # Below_Normal
        # make Below_Normal dominant inside the Maritime box (95..150 E, -10..7.5 N)
        xm = (X >= 95) & (X <= 150)
        ym = (Y >= -10) & (Y <= 7.5)
        box = np.outer(ym, xm)
        base = np.where(box, rng.uniform(45, 60, size=(ny, nx)), base)
        above = rng.uniform(15, 35, size=(ny, nx))
        normal = 100.0 - base - above
        # guard against negatives from the arithmetic
        normal = np.clip(normal, 1, None)
        s = base + normal + above
        prob[fi, li, 0] = (base   / s * 100).astype("float32")
        prob[fi, li, 1] = (normal / s * 100).astype("float32")
        prob[fi, li, 2] = (above  / s * 100).astype("float32")

# target_season[F, L] as short strings, e.g. Jul issuance -> ASO/SON/OND/NDJ
seasons = ["ASO", "SON", "OND", "NDJ"]
tgt = np.array([[seasons[li] for li in range(nl)] for _ in range(nf)])

with Dataset(OUT, "w", format="NETCDF4") as ds:
    ds.createDimension("X", nx)
    ds.createDimension("Y", ny)
    ds.createDimension("C", nc_)
    ds.createDimension("L", nl)
    ds.createDimension("F", nf)
    ds.createDimension("slen", 16)   # for string ids

    vX = ds.createVariable("X", "f4", ("X",)); vX[:] = X; vX.units = "degree_east"
    vY = ds.createVariable("Y", "f4", ("Y",)); vY[:] = Y; vY.units = "degree_north"
    vL = ds.createVariable("L", "f4", ("L",)); vL[:] = L; vL.units = "months"
    vF = ds.createVariable("F", "f4", ("F",)); vF[:] = F; vF.units = "months since 1960-01-01"

    # C as CHAR ids (unordered) — the whole point is selecting by NAME not index
    vC = ds.createVariable("C", "S1", ("C", "slen"))
    vC[:] = stringtochar(np.array(C_ids, dtype="S16"), encoding="ascii")
    vC.description = "tercile class ids; UNORDERED; select by name"

    vP = ds.createVariable("prob", "f4", ("F", "L", "C", "Y", "X"))
    vP[:] = prob; vP.units = "percent"

    vT = ds.createVariable("target_season", "S1", ("F", "L", "slen"))
    vT[:] = stringtochar(tgt.astype("S16"), encoding="ascii")

    ds.SYNTHETIC = "TRUE — garbage numbers, structure only. NOT FOR ARTICLE."

print(f"wrote {OUT}: prob shape {prob.shape} (F,L,C,Y,X); X {X[0]:.0f}..{X[-1]:.0f}; Y {Y[0]:.0f}..{Y[-1]:.0f}")
