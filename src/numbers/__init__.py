# brain_games.py
from game_engine import (
    welcome_user,
    run_game,
    generate_lcm_round,
    generate_progression_round
)


def select_game() -> str:
    print("Please select a game:")
    print("1. Least Common Multiple (LCM)")
    print("2. Geometric Progression")
    choice = input("Enter 1 or 2: ")
    while choice not in ['1', '2']:
        choice = input("Invalid input. Please enter 1 or 2: ")
    return choice


def main() -> None:
    name = welcome_user()
    game_choice = select_game()

    if game_choice == '1':
        run_game(
            game_rules="\nFind the smallest common multiple of given numbers.",
            generate_round=generate_lcm_round,
            name=name
        )
    else:
        run_game(
            game_rules="\nWhat number is missing in the progression?",
            generate_round=generate_progression_round,
            name=name
        )


if __name__ == "__main__":
    main()