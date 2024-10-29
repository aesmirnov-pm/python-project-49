import brain_games.engine as engine
import random
import brain_games.consts as consts

INSTRUCTION = consts.INSTRUCTION_PROGRESSION
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
    question = ' '.join(map(str, progression))
    return question, correct_answer


def run_progression_game():
    engine.run(return_question_and_answer, consts.INSTRUCTION_PROGRESSION)
