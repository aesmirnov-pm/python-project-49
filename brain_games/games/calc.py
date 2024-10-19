

import brain_games.engine as engine
import random
from brain_games.utils import get_random_number

INSTRUCTION = 'What is the result of the expression?'
LIST_OPERATOR = ['+', '-', '*']


def return_question_and_answer():
    number_1 = get_random_number()
    number_2 = get_random_number()
    operator = random.choice(LIST_OPERATOR)
    question = engine.question(number_1, operator, number_2)
    expression = f"{number_1}{operator}{number_2}"
    correct_answer = eval(expression)
    return question, correct_answer
