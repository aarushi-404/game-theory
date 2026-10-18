"""Small command-line demonstration for the cyber game theory project."""
from game_model import DEFAULT_ATTACKS, DEFAULT_DEFENSES, DEFAULT_PAYOFF, solve_zero_sum_game

def main():
    result = solve_zero_sum_game(DEFAULT_PAYOFF)
    print("Payoff matrix (attacker utility):")
    print(DEFAULT_PAYOFF)
    print("\nOptimal attacker mixed strategy:")
    for action, probability in zip(DEFAULT_ATTACKS, result["p"]):
        print(f"  {action}: {probability:.3f}")
    print("\nOptimal defender mixed strategy:")
    for action, probability in zip(DEFAULT_DEFENSES, result["q"]):
        print(f"  {action}: {probability:.3f}")
    print(f"\nEquilibrium expected attacker payoff: {result['value']:.3f}")
    print("Note: utilities are illustrative assumptions, not empirical measurements.")

if __name__ == "__main__":
    main()
