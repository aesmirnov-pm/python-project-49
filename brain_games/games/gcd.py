

import brain_games.engine as engine
import random

INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def greatest_common_divisor(number_1, number_2):
    min_number = min(number_1, number_2)
    max_number = max(number_1, number_2)
    while max_number % min_number != 0:
        max_number, min_number = min_number, max_number % min_number
    return min_number


def return_question_and_answer():
    number_1 = random.randint(2, 50)
    number_2 = random.randint(2, 50)
    question = engine.question(number_1, number_2)
    correct_answer = greatest_common_divisor(number_1, number_2)
    return question, correct_answer
