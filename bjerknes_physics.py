import numpy as np

def pressure(x, A, x0, w, base):
    """Idealised equatorial SLP using tanh profile."""
    return base - A * np.tanh((x - x0) / w)

def gradient(x, A, x0, w):
    """Analytic gradient dp/dx; peak negative at x0."""
    return -(A / w) * (1.0 / np.cosh((x - x0) / w))**2

def find_zero_crossings(xv, yv):
    s = np.sign(yv)
    out = []
    # Adding correctly extracts the array of indices from the tuple
    for i in np.where(np.diff(s) != 0)[0]:          # <-- [0] is essential
        out.append(xv[i] - yv[i] * (xv[i+1] - xv[i]) / (yv[i+1] - yv[i]))
    return out

def get_regime(dpbar, A1, A2):
    dA = A2 - A1
    if abs(dpbar) > abs(dA): return "B (No crossing)"
    if abs(dpbar) < 1e-5:    return "A (Coincident)"
    return "C (East of max)" if dpbar > 0 else "D (West of max)"

X = np.linspace(120, 270, 1200)