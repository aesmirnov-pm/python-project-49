import brain_games.engine as engine
from brain_games.utils import get_random_numbers
import brain_games.consts as consts


def is_even(num):
    return num % 2 == 0


def return_question_and_answer():
    random_num = get_random_numbers(1)[0]
    correct_answer = "yes" if is_even(random_num) else "no"
    question = str(random_num)
    return question, correct_answer


def run_even_game():
    engine.run(return_question_and_answer, consts.INSTRUCTION_EVEN)
