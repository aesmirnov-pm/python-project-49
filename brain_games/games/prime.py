

import brain_games.engine as engine
import random

INSTRUCTION = ('Answer "yes" if given number is prime. '
               'Otherwise answer "no".')


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def return_question_and_answer():
    number = random.randint(1, 200)
    question = engine.question(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer
