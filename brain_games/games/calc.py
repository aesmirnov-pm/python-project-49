#!/usr/bin/env python3


import brain_games.engine as engine
import prompt
import random
import brain_games.consts as consts
import brain_games.utils as utils


def main():
    name = engine.welcome()
    print(consts.CALC_INSTRUCTION)
    i = 0
    while i < consts.REPEATS:
        number_1 = utils.random_number_from_0_to_20()
        number_2 = utils.random_number_from_0_to_20()
        index = random.randint(0, 2)
        list_operator = ['+', '-', '*']
        engine.question(number_1, list_operator[index], number_2)
        answer_user = prompt.string(consts.YOUR_ANSWER)
        expression = str(number_1) + list_operator[index] + str(number_2)
        answer_correct = eval(expression)
        if engine.print_result(name, str(answer_correct), answer_user) is False:
            return
        i += 1
    engine.congrats(name)


if __name__ == '__main__':
    main()
