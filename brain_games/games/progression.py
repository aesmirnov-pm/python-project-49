

import brain_games.engine as engine
import random

INSTRUCTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 9


def return_question_and_answer():
    first_num = random.randint(2, 15)
    step = random.randint(2, 5)
    missed_num_ind = random.randint(0, PROGRESSION_LENGTH)
    progression = [
        '..' if i == missed_num_ind else str(first_num + i * step)
        for i in range(PROGRESSION_LENGTH)
    ]
    correct_answer = first_num + step * missed_num_ind
    question = engine.question(*progression)
    return question, correct_answer
