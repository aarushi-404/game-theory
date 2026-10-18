# Game-Theoretic Analysis of Cyber Attack and Defense Strategies

## Abstract
This project demonstrates how game theory can model strategic interactions between cyber attackers and security defenders. A finite two-player zero-sum game is represented using an attacker utility matrix. Linear programming computes optimal mixed strategies and the equilibrium expected utility. An interactive Streamlit dashboard allows the user to inspect the matrix, edit utility assumptions, and compare hypothetical defensive scenarios.

## Problem Statement
Attackers and defenders make decisions while anticipating the actions of the other side. Security teams have finite resources and must select controls that reduce an adversary's expected advantage. A game-theoretic model provides a structured way to reason about such strategic choices.

## Objectives
1. Represent attacker and defender actions as strategies in a finite game.
2. Define a utility matrix for action pairs.
3. Compute optimal mixed strategies and equilibrium utility.
4. Visualize payoffs and compare illustrative scenarios.
5. Build an interactive interface for demonstrating the model.

## Methodology
The attacker selects a row and the defender selects a column. Each cell gives attacker utility. The attacker maximizes expected utility, and the defender minimizes it. A linear-programming formulation computes equilibrium mixed strategies. The app uses hypothetical utility scores for demonstration.

## Implementation
The implementation uses Python, NumPy, SciPy, Pandas, Matplotlib and Streamlit. `game_model.py` contains the zero-sum game solver; `app.py` displays the payoff matrix, equilibrium strategies, heatmap and scenario comparison; `simulation.py` provides a terminal demonstration.

## Results
When run, the dashboard reports the optimal probability assigned to each attacker and defender strategy, the equilibrium expected attacker payoff, and whether a pure-strategy saddle point exists. The user can alter matrix entries to explore how assumptions change the model's recommendations. Insert screenshots captured from the actual running application here.

## Limitations
The model assumes zero-sum preferences, known utilities and rational players. Real cybersecurity involves uncertainty, incomplete information, non-zero-sum incentives, changing environments and dependencies between controls. The scores are illustrative and do not establish real-world attack success probabilities.

## Conclusion
The project provides a working educational simulator for strategic cyber defense analysis. It demonstrates payoff matrices, mixed strategies, linear programming and equilibrium concepts through an interactive visualization. Future work could incorporate Bayesian games, repeated games, uncertainty in utilities, and evidence-based cost or risk estimates.

## References
1. von Neumann, J., & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*. Princeton University Press.
2. Nash, J. (1950). Equilibrium points in n-person games. *Proceedings of the National Academy of Sciences*, 36(1), 48–49.
3. Osborne, M. J. (2004). *An Introduction to Game Theory*. Oxford University Press.
4. SciPy documentation, `scipy.optimize.linprog`.
5. Streamlit documentation.
