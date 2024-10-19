

import brain_games.engine as engine
import random
from brain_games.utils import get_random_number

INSTRUCTION = 'What is the result of the expression?'


def return_question_and_answer():
    number_1 = get_random_number()
    number_2 = get_random_number()
    index = random.randint(0, 2)
    list_operator = ['+', '-', '*']
    question = engine.question(number_1, list_operator[index], number_2)
    expression = str(number_1) + list_operator[index] + str(number_2)
    correct_answer = eval(expression)
    return question, correct_answer
