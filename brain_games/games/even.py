

import brain_games.engine as engine
from brain_games.utils import get_random_number

INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def return_question_and_answer():
    random_num = get_random_number()
    correct_answer = "yes" if is_even(random_num) else "no"
    question = engine.question(random_num)
    return question, correct_answer
