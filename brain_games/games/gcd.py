import brain_games.engine as engine
import random
import math
import brain_games.consts as consts


def return_question_and_answer():
    number_1, number_2 = random.sample(range(2, 50), 2)
    question = f'{number_1} {number_2}'
    correct_answer = math.gcd(number_1, number_2)
    return question, correct_answer


def run_gcd_game():
    engine.run(return_question_and_answer, consts.INSTRUCTION_GCD)
