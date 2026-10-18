# Game-Theoretic Analysis of Cyber Attack and Defense Strategies

An educational Python project that models an attacker and defender as players in a finite, zero-sum game. It calculates equilibrium mixed strategies using linear programming and presents the results in a Streamlit dashboard.

## Features
- Editable attacker-payoff matrix
- Optimal mixed strategies for attacker and defender
- Equilibrium expected utility
- Pure-strategy saddle point check
- Payoff heatmap
- Comparison of illustrative security scenarios
- CLI output for quick testing

## Setup
Use Python 3.10 or newer.

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows:
# .venv\Scripts\activate

pip install -r requirements.txt
```

## Run the dashboard
```bash
streamlit run app.py
```
Open the local URL printed by Streamlit (usually http://localhost:8501).

## Run the command-line demonstration
```bash
python simulation.py
```

## Model assumptions
- The payoff matrix is from the attacker's perspective.
- The attacker maximizes expected utility; the defender minimizes it.
- The model is zero-sum and assumes both players know the payoff matrix.
- Scores are hypothetical utility values used for teaching and demonstration. They are not attack probabilities, measured losses, or empirical security effectiveness.
- The app does not connect to networks, scan systems, send packets, or execute cyberattacks.

## Files
- `app.py`: Streamlit user interface
- `game_model.py`: linear-programming equilibrium solver
- `simulation.py`: command-line example
- `requirements.txt`: Python dependencies
- `screenshots/`: folder for screenshots of the running app

## Suggested screenshots for the report
1. Main dashboard and default payoff matrix
2. Optimal mixed strategies and equilibrium value
3. Payoff heatmap
4. Scenario comparison after editing the matrix
