#!/usr/bin/env python3


import brain_games.engine as engine
import prompt
import random
import brain_games.consts as consts
import brain_games.utils as utils

def is_even(num):
    return num % 2 == 0


def main():
    name = engine.welcome()
    print(consts.EVEN_INSTRUCTION)
    i = 0
    while i < consts.REPEATS:
        random_num = utils.random_number_from_0_to_20()
        engine.question(random_num)
        answer_user = prompt.string(consts.YOUR_ANSWER)
        if is_even(random_num):
            correct_answer = consts.YES
        else:
            correct_answer = consts.NO
        if engine.print_result(name, correct_answer, answer_user) is False:
            return
        i += 1
    engine.congrats(name)


if __name__ == '__main__':
    main()
