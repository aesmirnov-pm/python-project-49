import brain_games.engine as engine
import random

INSTRUCTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def return_question_and_answer():
    first_num = random.randint(2, 15)
    step = random.randint(2, 5)
    missed_num_ind = random.randint(0, PROGRESSION_LENGTH - 1)
    progression = [
        str(i)
        for i in range(first_num, first_num + step * PROGRESSION_LENGTH, step)
    ]
    progression[missed_num_ind] = '..'
    correct_answer = first_num + step * missed_num_ind
    question = engine.question(*progression)
    return question, correct_answer
