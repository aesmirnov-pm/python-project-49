import brain_games.engine as engine
import random
from brain_games.utils import get_random_number
from operator import add, sub, mul

INSTRUCTION = 'What is the result of the expression?'
OPERATOR = {
    '+': add,
    '*': mul,
    '-': sub,
}


def return_question_and_answer():
    number_1 = get_random_number()
    number_2 = get_random_number()
    operator = random.choice(list(OPERATOR.keys()))
    correct_answer = OPERATOR[operator](number_1, number_2)
    question = engine.question(number_1, operator, number_2)
    return question, str(correct_answer)
