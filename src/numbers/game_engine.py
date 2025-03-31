# game_engine.py
import random
from typing import Tuple, Callable


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def run_game(game_rules: str, generate_round: Callable[[], Tuple[str, str]], name: str, rounds: int = 3) -> None:
    """
    Основной движок игры
    :param game_rules: Правила игры для показа пользователю
    :param generate_round: Функция генерации раунда (возвращает вопрос и правильный ответ)
    :param name: Имя игрока
    :param rounds: Количество раундов (по умолчанию 3)
    """
    print(game_rules)

    for _ in range(rounds):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")


def generate_lcm_round() -> Tuple[str, str]:
    """Генерация раунда для игры НОК"""
    a, b, c = random.randint(1, 30), random.randint(1, 30), random.randint(1, 30)
    question = f"{a} {b} {c}"
    correct_answer = str(lcm_of_three(a, b, c))
    return question, correct_answer


def generate_progression_round() -> Tuple[str, str]:
    """Генерация раунда для игры Прогрессия"""
    progression = generate_geometric_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer


def gcd(a: int, b: int) -> int:
    """Вычисляет наибольший общий делитель"""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Вычисляет наименьшее общее кратное"""
    return a * b // gcd(a, b)


def lcm_of_three(a: int, b: int, c: int) -> int:
    return lcm(lcm(a, b), c)


def generate_geometric_progression() -> list[int]:
    """Генерирует геометрическую прогрессию"""
    start = random.randint(1, 5)
    step = random.randint(2, 5)
    length = random.randint(5, 10)
    return [start * (step ** i) for i in range(length)]