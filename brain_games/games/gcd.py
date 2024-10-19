
import brain_games.engine as engine
import random
import math

INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def return_question_and_answer():
    number_1 = random.randint(2, 50)
    number_2 = random.randint(2, 50)
    question = engine.question(number_1, number_2)
    correct_answer = math.gcd(number_1, number_2)
    return question, correct_answer
