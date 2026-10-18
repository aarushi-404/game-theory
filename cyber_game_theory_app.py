import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from game_model import DEFAULT_ATTACKS, DEFAULT_DEFENSES, DEFAULT_PAYOFF, solve_zero_sum_game, pure_saddle_point

st.set_page_config(page_title="Cyber Game Theory Simulator", page_icon="🛡️", layout="wide")
st.title("Game-Theoretic Analysis of Cyber Attack and Defense Strategies")
st.caption("Educational decision-support simulator using hypothetical utility scores. No real attacks are performed.")

st.sidebar.header("Scenario settings")
st.sidebar.write("Adjust the attacker's utility for each attacker–defender action pair.")
st.sidebar.info("Higher values favor the attacker; lower values favor the defender. Values are illustrative, not measured probabilities.")

attacks = DEFAULT_ATTACKS
defenses = DEFAULT_DEFENSES
default = DEFAULT_PAYOFF.astype(float)

edited = st.sidebar.checkbox("Customize payoff matrix", value=False)
if edited:
    st.sidebar.subheader("Edit utilities")
    payoff = default.copy()
    for i, attack in enumerate(attacks):
        for j, defense in enumerate(defenses):
            payoff[i, j] = st.sidebar.number_input(
                f"{attack} × {defense}", min_value=-20.0, max_value=20.0,
                value=float(default[i, j]), step=1.0, key=f"p_{i}_{j}"
            )
else:
    payoff = default

col1, col2, col3 = st.columns(3)
col1.metric("Attacker actions", len(attacks))
col2.metric("Defender actions", len(defenses))
col3.metric("Game type", "Zero-sum")

st.subheader("Attacker payoff matrix")
df = pd.DataFrame(payoff, index=attacks, columns=defenses)
st.dataframe(df.style.format("{:.1f}"), use_container_width=True)

solution = solve_zero_sum_game(payoff)
pure = pure_saddle_point(payoff)

left, right = st.columns(2)
with left:
    st.subheader("Optimal mixed strategies")
    st.write("**Attacker strategy**")
    st.dataframe(pd.DataFrame({"Action": attacks, "Probability": solution["p"]}).style.format({"Probability":"{:.1%}"}), hide_index=True, use_container_width=True)
    st.write("**Defender strategy**")
    st.dataframe(pd.DataFrame({"Action": defenses, "Probability": solution["q"]}).style.format({"Probability":"{:.1%}"}), hide_index=True, use_container_width=True)
    st.metric("Equilibrium expected attacker payoff", f'{solution["value"]:.3f}')
    if pure:
        st.success(f"Pure-strategy saddle point exists: {attacks[pure[0]]} vs {defenses[pure[1]]}, value {pure[2]:.2f}.")
    else:
        st.info("No pure-strategy saddle point for this matrix; mixed strategies are used.")

with right:
    st.subheader("Payoff heatmap")
    fig, ax = plt.subplots(figsize=(7, 4.5))
    im = ax.imshow(payoff, cmap="RdYlBu_r", aspect="auto")
    ax.set_xticks(range(len(defenses)), defenses, rotation=20, ha="right")
    ax.set_yticks(range(len(attacks)), attacks)
    ax.set_title("Attacker utility by action pair")
    for i in range(payoff.shape[0]):
        for j in range(payoff.shape[1]):
            ax.text(j, i, f"{payoff[i,j]:.1f}", ha="center", va="center", color="black")
    fig.colorbar(im, ax=ax, label="Attacker utility")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

st.subheader("Scenario comparison")
scenarios = {
    "Baseline": DEFAULT_PAYOFF.astype(float),
    "Stronger phishing resistance": np.array([[-2, 4, 1], [5, -6, 2], [3, 2, -4]], dtype=float),
    "Enhanced monitoring": np.array([[-2, 4, -2], [5, -3, -1], [3, 2, -7]], dtype=float),
}
rows = []
for name, matrix in scenarios.items():
    result = solve_zero_sum_game(matrix)
    rows.append({"Scenario": name, "Equilibrium payoff": result["value"], "Interpretation": "Lower is better for defender"})
scenario_df = pd.DataFrame(rows)
st.dataframe(scenario_df.style.format({"Equilibrium payoff":"{:.3f}"}), hide_index=True, use_container_width=True)

fig2, ax2 = plt.subplots(figsize=(8, 3.5))
ax2.bar(scenario_df["Scenario"], scenario_df["Equilibrium payoff"])
ax2.axhline(0, linewidth=0.8)
ax2.set_ylabel("Equilibrium attacker utility")
ax2.set_title("Illustrative scenario comparison")
ax2.tick_params(axis="x", rotation=12)
fig2.tight_layout()
st.pyplot(fig2)
plt.close(fig2)

with st.expander("How to interpret the model"):
    st.markdown("""
    - The attacker chooses a row; the defender chooses a column.
    - Each cell is a hypothetical utility score from the attacker's perspective.
    - The attacker maximizes expected utility while the defender minimizes it.
    - The linear-programming solution gives optimal mixed strategies for this zero-sum model.
    - Scores are assumptions for demonstrating the method. They are not empirical risk estimates.
    - This is a strategic simulation only; it does not scan networks, send traffic, or execute attacks.
    """)

st.caption("Project prototype • Python + Streamlit + NumPy + SciPy + Matplotlib")
