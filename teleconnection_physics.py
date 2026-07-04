"""
teleconnection_physics.py — Idealised meridional (latitude-height) field
generators for the ENSO -> Hadley -> jet teleconnection atlas (Notebook 2).

This is the meridional counterpart to `bjerknes_physics.py` (which handles the
zonal Walker axis). The two notebooks are perpendicular views of one ENSO
taxonomy, so they intentionally use *separate* models; this module holds the
latitude-height generators that Notebook 2 used to define inline.

All generators are pure functions of the passed `lat` (deg N) and `height` (km)
axes — they derive their output shape (n_height, n_lat) from those arrays and do
not depend on any module-level grid, so they can be reused and unit-tested with
any domain.

Model constants (tuning parameters, NOT physical constants — in a GCM these
would emerge from solving the full equations):
    Z_MID   height (km) where the pressure anomaly changes sign (the sign-flip level)
    H_CELL  vertical extent (km) of the Hadley circulation
    SCALE_P hPa per (degC * km): converts SST anomaly and height into pressure anomaly
"""
import numpy as np

Z_MID = 7.0     # km: pressure-anomaly sign-flip level (below => low surface P; above => high aloft)
H_CELL = 14.0   # km: vertical extent of the Hadley cell (streamfunction closes at 0 and H_CELL)
SCALE_P = 0.6   # hPa / (degC * km): magnitude scaling; real ENSO anomalies ~ +/-5-15 hPa


def gen_sst(lat, amp, gradient, width, center_lat=5):
    """Equator-to-pole SST anomaly. Gaussian bump (gradient=True) or flat (uniform offset)."""
    lat = np.asarray(lat, dtype=float)
    if gradient:
        return amp * np.exp(-((lat - center_lat) ** 2) / (2 * width ** 2))
    return amp * np.ones_like(lat)


def gen_pressure(lat, height, amp, gradient, width, center_lat):
    """Pressure anomaly tied to SST: a warm column => low surface / high aloft.

        p(lat, z) = SST(lat) * (z - Z_MID) * SCALE_P

    Below Z_MID: (z - Z_MID) < 0, so warm SST => negative p (low pressure).
    Above Z_MID: (z - Z_MID) > 0, so warm SST => positive p (high pressure).

    Keystone (Scenario B): uniform SST (gradient=False) makes SST constant in
    latitude, so p(lat, z) has no latitude dependence => contours are perfectly
    horizontal => no meridional pressure gradient => no driver for the Hadley
    cell, however large the SST magnitude. (This is asserted in the tests.)
    """
    lat = np.asarray(lat, dtype=float)
    height = np.asarray(height, dtype=float)
    sstp = gen_sst(lat, amp, gradient, width, center_lat)
    P = np.zeros((height.size, lat.size))
    for i, z in enumerate(height):
        P[i, :] = sstp * (z - Z_MID) * SCALE_P
    return P


def gen_hadley(lat, height, strength, descent_lat):
    """Closed thermally-direct Hadley cell from a streamfunction.

        psi  = strength * sin(pi * xi) * sin(pi * zeta),   xi = lat/descent_lat, zeta = z/H_CELL
        v    = -d(psi)/dz     (poleward, +)
        w    = +d(psi)/dlat   (upward, +)

    Rising at the equator, poleward aloft, sinking at descent_lat, equatorward
    return at the surface. Deriving (v, w) from a streamfunction makes meridional
    continuity hold identically. Zero outside 0 <= lat <= descent_lat and
    0 <= z <= H_CELL. Planar approximation (spherical cos(lat) weighting omitted).
    """
    lat = np.asarray(lat, dtype=float)
    height = np.asarray(height, dtype=float)
    v = np.zeros((height.size, lat.size))
    w = np.zeros((height.size, lat.size))
    for i, z in enumerate(height):
        if z > H_CELL:
            continue
        zeta = z / H_CELL
        in_cell = lat <= descent_lat
        xi = np.where(in_cell, lat / descent_lat, 0.0)
        v_row = -strength * np.sin(np.pi * xi) * (np.pi / H_CELL) * np.cos(np.pi * zeta)
        w_row = +strength * (np.pi / descent_lat) * np.cos(np.pi * xi) * np.sin(np.pi * zeta)
        v[i, :] = np.where(in_cell, v_row, 0.0)
        w[i, :] = np.where(in_cell, w_row, 0.0)
    return v, w


def gen_zonal_wind(lat, height, mf, descent_lat):
    """Upper-tropospheric zonal wind: a subtropical westerly jet at descent_lat
    (~12 km) plus tropical upper-level easterlies. Jet amplitude scales with the
    momentum flux `mf`. The jet core sits at descent_lat — the poleward edge of
    the Hadley cell — where the poleward momentum transport converges.
    """
    lat = np.asarray(lat, dtype=float)
    height = np.asarray(height, dtype=float)
    jet_amp = 30.0 * mf + 2.0
    U = np.zeros((height.size, lat.size))
    for i, z in enumerate(height):
        westerly = jet_amp * np.exp(-((lat - descent_lat) / 6.0) ** 2) * \
                   np.exp(-((z - 12.0) / 2.5) ** 2)
        easterly = 8.0 * np.exp(-((lat - 8.0) / 8.0) ** 2) * \
                   np.exp(-((z - 13.0) / 3.0) ** 2)
        U[i, :] = westerly - easterly
    return U


def gen_momentum_flux(lat, height, mf, descent_lat):
    """Magnitude of poleward angular-momentum transport in the upper branch.

    Peaks a few degrees EQUATORWARD of descent_lat (~13 km altitude) and fades
    poleward, so transport visibly converges ONTO descent_lat — the latitude
    where gen_zonal_wind places the subtropical jet. Scales with `mf`.
    """
    lat = np.asarray(lat, dtype=float)
    height = np.asarray(height, dtype=float)
    flux_lat = descent_lat - 5.0          # transport peaks equatorward of the jet core
    F = np.zeros((height.size, lat.size))
    for i, z in enumerate(height):
        F[i, :] = mf * np.exp(-((lat - flux_lat) / 11.0) ** 2) * \
                  np.exp(-((z - 13.0) / 1.5) ** 2)
    return F
