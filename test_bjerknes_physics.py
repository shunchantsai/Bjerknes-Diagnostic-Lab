"""
test_bjerknes_physics.py — sanity + physics-claim tests for bjerknes_physics.py

Run either way (numpy is the only requirement — no pytest needed):
    pytest test_bjerknes_physics.py     # if pytest is installed
    python test_bjerknes_physics.py     # zero extra deps; prints PASS/FAIL summary

Each test guards a *specific claim the notebooks make*, so a regression that
would silently change a figure or a regime label fails loudly instead.
"""
import numpy as np
import bjerknes_physics as bp

X0 = bp.X0_COLD          # 178.0 — cold-year node / gradient-maximum longitude
W = 22.0                 # atmospheric branch width (deg lon)
BASE = 1010.0


# --- Regime classifier (the A/B/C/D taxonomy) -------------------------------

def test_get_regime_four_cases():
    assert bp.get_regime(0.0, 0.7).startswith("A")    # node on the max
    assert bp.get_regime(1.0, 0.7).startswith("B")    # |offset| >= |delta| -> no node
    assert bp.get_regime(0.3, 0.7).startswith("C")    # node displaced east
    assert bp.get_regime(-0.3, 0.7).startswith("D")   # node displaced west


def test_get_regime_boundary_is_B():
    # exactly at threshold -> no crossing (B), via the 1e-9 guard
    assert bp.get_regime(0.7, 0.7).startswith("B")


# --- Zero-crossing finder ---------------------------------------------------

def test_find_zero_crossings_simple_linear():
    x = np.linspace(-1, 1, 101)
    y = x.copy()                              # crosses zero at 0
    cr = bp.find_zero_crossings(x, y)
    assert len(cr) == 1
    assert abs(cr[0]) < 1e-6
    assert isinstance(cr[0], float)           # float, not a 1-element array


def test_find_zero_crossings_none_when_all_positive():
    x = np.linspace(0, 10, 50)
    y = np.ones_like(x)
    assert bp.find_zero_crossings(x, y) == []


# --- Gradient geometry ------------------------------------------------------

def test_gradient_extremum_at_x0():
    X = bp.DEFAULT_X
    g = bp.gradient(X, 4.0, X0, W)            # -(A/w) sech^2 -> most negative at x0
    assert abs(X[np.argmin(g)] - X0) < 0.2
    assert abs(X[np.argmax(np.abs(g))] - X0) < 0.2


def test_gradient_is_derivative_of_pressure():
    X = np.linspace(120, 270, 4000)
    p = bp.pressure(X, 4.0, X0, W, BASE, global_offset=0.0)
    g_analytic = bp.gradient(X, 4.0, X0, W)
    g_numeric = np.gradient(p, X)
    # compare the interior (np.gradient edges are one-sided / less accurate)
    assert np.allclose(g_numeric[5:-5], g_analytic[5:-5], atol=1e-4)


# --- The two structural claims of Part 1 (zonal) ----------------------------

def test_scenario_A_node_coincides_with_gradient_max():
    # global_offset = 0  ->  the zero isallobar sits ON the gradient maximum
    X = bp.DEFAULT_X
    dp = (bp.pressure(X, 4.2, X0, W, BASE, global_offset=0.0)
          - bp.pressure(X, 3.5, X0, W, BASE, global_offset=0.0))
    crossings = bp.find_zero_crossings(X, dp)
    assert len(crossings) == 1
    node = crossings[0]
    grad_max_lon = X[np.argmax(np.abs(bp.gradient(X, 4.2, X0, W)))]
    assert abs(node - X0) < 0.2
    assert abs(node - grad_max_lon) < 0.5     # the coincidence itself


def test_scenario_B_offset_erases_the_node():
    # |global_offset| >= delta_amp  ->  no crossing anywhere
    X = bp.DEFAULT_X
    dp = (bp.pressure(X, 4.2, X0, W, BASE, global_offset=1.0)
          - bp.pressure(X, 3.5, X0, W, BASE, global_offset=0.0))
    assert bp.find_zero_crossings(X, dp) == []
    assert bp.get_regime(1.0, 4.2 - 3.5).startswith("B")


def test_seesaw_orientation_high_west_low_east():
    # positive so_amplitude -> pressure higher in the west (x<x0) than east (x>x0)
    west = bp.pressure(120.0, 4.0, X0, W, BASE)
    east = bp.pressure(240.0, 4.0, X0, W, BASE)
    assert west > east


# --- SST tongue + the "structure beats magnitude" width thesis --------------

def test_sst_tongue_peak_depth_at_x0():
    assert abs(bp.sst_tongue(X0, 4.0, X0, W) - (-4.0)) < 1e-9


def test_total_pressure_drop_approx_2A():
    A = 3.0
    drop = bp.total_pressure_drop(A, X0, W)
    assert abs(drop - 2 * A) < 0.2 * A        # ~2A, up to finite-domain truncation


def test_structure_beats_magnitude_width_discrimination():
    # THE central thesis: the content integral SEES width; the pressure-drop
    # integral is BLIND to it. This is what makes the 1963-vs-1965 point work.
    depth, A = 4.0, 1.0
    w_narrow, w_wide = 15.0, 30.0
    content_ratio = (bp.integrated_cold_content(depth, X0, w_wide)
                     / bp.integrated_cold_content(depth, X0, w_narrow))
    drop_ratio = (bp.total_pressure_drop(A, X0, w_wide)
                  / bp.total_pressure_drop(A, X0, w_narrow))
    assert content_ratio > 1.7                # ~2x  (content ~ depth * w)
    assert 0.9 < drop_ratio < 1.1             # ~1x  (drop ~ 2A, width-blind)


# --- Oceanic memory (leaky integrator) --------------------------------------

def test_oceanic_memory_sustained_wider_than_interrupted():
    # SAME instantaneous forcing at the endpoint, different history -> different
    # width, because the ocean integrates slowly (the lag-asymmetry claim).
    months = 60
    f_sustained = np.ones(months)
    f_interrupted = np.ones(months)
    f_interrupted[months - 21: months - 3] = 0.0   # warm interruption, then resume
    w_sus = bp.tongue_width_history(f_sustained, tau=18.0, w0=5.0, gain=20.0)
    w_int = bp.tongue_width_history(f_interrupted, tau=18.0, w0=5.0, gain=20.0)
    assert w_sus[-1] > w_int[-1]                     # memory: sustained -> wider
    assert np.all(np.diff(w_sus) >= -1e-9)           # sustained forcing -> monotonic build


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
