"""
test_teleconnection_physics.py — physics-claim tests for teleconnection_physics.py
(the meridional ENSO -> Hadley -> jet generators used by Notebook 2).

Run either way (numpy only):
    pytest test_teleconnection_physics.py
    python test_teleconnection_physics.py
"""
import numpy as np
import teleconnection_physics as tp

LAT = np.linspace(0, 60, 160)      # equator -> 60 N
HGT = np.linspace(0, 16, 130)      # surface -> 16 km


# --- SST forcing ------------------------------------------------------------

def test_gen_sst_gradient_peaks_at_center_lat():
    sst = tp.gen_sst(LAT, amp=2.0, gradient=True, width=20, center_lat=5)
    assert abs(LAT[np.argmax(sst)] - 5) < 0.5
    # peak ~ amp; slightly below because the grid samples near, not exactly at, center_lat
    assert 1.99 < sst.max() <= 2.0 + 1e-9

def test_gen_sst_uniform_is_flat():
    sst = tp.gen_sst(LAT, amp=2.5, gradient=False, width=60, center_lat=5)
    assert np.allclose(sst, 2.5)


# --- Pressure: vertical sign reversal + the Scenario-B keystone --------------

def test_gen_pressure_sign_reverses_across_Z_MID():
    # warm column: low pressure below Z_MID, high pressure above it
    P = tp.gen_pressure(LAT, HGT, amp=2.0, gradient=True, width=20, center_lat=5)
    jpk = np.argmax(np.abs(tp.gen_sst(LAT, 2.0, True, 20, 5)))   # warmest latitude
    below = P[HGT < tp.Z_MID, jpk]
    above = P[HGT > tp.Z_MID, jpk]
    assert np.all(below < 0)      # low surface pressure under a warm column
    assert np.all(above > 0)      # high pressure aloft

def test_scenario_B_uniform_SST_kills_the_meridional_gradient():
    # THE keystone claim, made executable: uniform warm SST -> pressure has no
    # latitude dependence -> zero meridional gradient -> no Hadley driver,
    # however large the SST magnitude.
    P = tp.gen_pressure(LAT, HGT, amp=2.5, gradient=False, width=60, center_lat=5)
    for i in range(P.shape[0]):
        assert np.allclose(P[i, :], P[i, 0])          # each height row is flat in latitude
    assert np.max(np.abs(np.gradient(P, LAT, axis=1))) < 1e-9

def test_gradient_SST_does_create_a_driver():
    # the contrast case: a real SST gradient DOES produce a meridional gradient
    P = tp.gen_pressure(LAT, HGT, amp=2.0, gradient=True, width=20, center_lat=5)
    assert np.max(np.abs(np.gradient(P, LAT, axis=1))) > 1e-3


# --- Hadley cell topology ---------------------------------------------------

def test_hadley_zero_outside_the_cell():
    v, w = tp.gen_hadley(LAT, HGT, strength=1.0, descent_lat=30)
    poleward = LAT > 30                       # outside the cell
    assert np.allclose(v[:, poleward], 0.0)
    assert np.allclose(w[:, poleward], 0.0)

def test_hadley_rises_at_the_equator():
    v, w = tp.gen_hadley(LAT, HGT, strength=1.0, descent_lat=30)
    zmid = np.argmin(np.abs(HGT - tp.H_CELL / 2))   # mid-cell height
    assert w[zmid, 0] > 0                             # upward motion at the equator


# --- Jet + momentum transport co-location -----------------------------------

def test_momentum_flux_peaks_equatorward_of_descent_lat():
    F = tp.gen_momentum_flux(LAT, HGT, mf=1.0, descent_lat=30)
    z13 = np.argmin(np.abs(HGT - 13))
    assert LAT[np.argmax(F[z13, :])] < 30            # transport converges onto the jet

def test_jet_core_sits_near_descent_lat():
    U = tp.gen_zonal_wind(LAT, HGT, mf=1.0, descent_lat=30)
    z12 = np.argmin(np.abs(HGT - 12))
    assert abs(LAT[np.argmax(U[z12, :])] - 30) < 4


# --- Purity: generators depend only on the passed grid ----------------------

def test_generators_are_pure_on_arbitrary_grids():
    lat = np.linspace(0, 60, 20)
    hgt = np.linspace(0, 16, 10)
    assert tp.gen_pressure(lat, hgt, 2.0, True, 20, 5).shape == (10, 20)
    v, w = tp.gen_hadley(lat, hgt, 1.0, 30)
    assert v.shape == (10, 20) and w.shape == (10, 20)


if __name__ == "__main__":
    import sys
    tests = [v for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"PASS  {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {t.__name__}: {e}")
        except Exception as e:            # noqa: BLE001
            failed += 1
            print(f"ERROR {t.__name__}: {type(e).__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
