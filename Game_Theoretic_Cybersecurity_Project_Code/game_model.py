import numpy as np
from scipy.optimize import linprog

DEFAULT_ATTACKS = ["Web server targeting", "Phishing attempt", "Denial of service"]
DEFAULT_DEFENSES = ["Firewall", "Multi-factor authentication", "Monitoring"]
DEFAULT_PAYOFF = np.array([
    [-2,  4,  1],
    [ 5, -3,  2],
    [ 3,  2, -4]
], dtype=float)

def solve_zero_sum_game(payoff):
    """Solve a finite two-player zero-sum game using linear programming.

    payoff[i,j] is the attacker's utility. The attacker maximizes it;
    the defender minimizes it. Returns optimal mixed strategies and value.
    """
    A = np.asarray(payoff, dtype=float)
    if A.ndim != 2 or min(A.shape) < 1:
        raise ValueError("payoff must be a non-empty 2D matrix")
    if not np.isfinite(A).all():
        raise ValueError("payoff matrix must contain finite numbers")

    # Shift payoffs so all entries are strictly positive; probabilities are unchanged.
    shift = max(0.0, 1.0 - float(A.min()))
    B = A + shift
    m, n = B.shape

    # Attacker: maximize sum(x), subject to B.T @ x <= 1, x >= 0.
    # Normalize p = x / sum(x); game value on shifted matrix is 1/sum(x).
    attacker_lp = linprog(
        c=-np.ones(m),
        A_ub=B.T,
        b_ub=np.ones(n),
        bounds=[(0, None)] * m,
        method="highs"
    )
    if not attacker_lp.success:
        raise RuntimeError(f"Attacker optimization failed: {attacker_lp.message}")
    x = attacker_lp.x
    x_sum = x.sum()
    p = x / x_sum
    shifted_value = 1.0 / x_sum
    value = shifted_value - shift

    # Defender: minimize sum(y), subject to B @ y >= 1, y >= 0.
    defender_lp = linprog(
        c=np.ones(n),
        A_ub=-B,
        b_ub=-np.ones(m),
        bounds=[(0, None)] * n,
        method="highs"
    )
    if not defender_lp.success:
        raise RuntimeError(f"Defender optimization failed: {defender_lp.message}")
    y = defender_lp.x
    y_sum = y.sum()
    q = y / y_sum

    # Numerical consistency: compute expected value from the returned strategies.
    value_from_strategies = float(p @ A @ q)
    return {
        "p": p,
        "q": q,
        "value": value,
        "value_from_strategies": value_from_strategies,
        "attacker_lp_success": attacker_lp.success,
        "defender_lp_success": defender_lp.success,
    }

def pure_saddle_point(payoff, tol=1e-9):
    """Return (row, column, value) if a pure saddle point exists; otherwise None."""
    A = np.asarray(payoff, dtype=float)
    row_mins = A.min(axis=1)
    col_maxs = A.max(axis=0)
    maximin = row_mins.max()
    minimax = col_maxs.min()
    if abs(maximin - minimax) <= tol:
        candidates = np.argwhere(np.isclose(A, maximin, atol=tol))
        for i, j in candidates:
            if np.isclose(row_mins[i], maximin, atol=tol) and np.isclose(col_maxs[j], minimax, atol=tol):
                return int(i), int(j), float(A[i, j])
    return None
