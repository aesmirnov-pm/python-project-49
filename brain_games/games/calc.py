import brain_games.engine as engine
import random
from brain_games.utils import get_random_numbers
import brain_games.consts as consts


def get_random_math_sign_and_result(first_num, second_num):
    return random.choice([
        ('+', first_num + second_num),
        ('-', first_num - second_num),
        ('*', first_num * second_num)
    ])


def return_question_and_answer():
    number_1, number_2 = get_random_numbers(2)
    operator, correct_answer = (
        get_random_math_sign_and_result(number_1, number_2)
    )
    question = engine.question(number_1, operator, number_2)
    return question, str(correct_answer)


def run_calc_game():
    engine.run(return_question_and_answer, consts.INSTRUCTION_CALC)
