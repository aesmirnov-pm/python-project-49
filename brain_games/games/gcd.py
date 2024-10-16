#!/usr/bin/env python3


import brain_games.engine as engine
import prompt
import random
import brain_games.consts as consts


def greatest_common_divisor(number_1, number_2):
    min_number = min(number_1, number_2)
    max_number = max(number_1, number_2)
    while max_number % min_number != 0:
        max_number, min_number = min_number, max_number % min_number
    return min_number


def main():
    name = engine.welcome()
    print(consts.GCD_INSTRUCTION)
    i = 0
    while i < consts.REPEATS:
        number_1 = random.randint(2, 50)
        number_2 = random.randint(2, 50)
        engine.question(number_1, number_2)
        answer_user = prompt.string(consts.YOUR_ANSWER)
        answer_correct = greatest_common_divisor(number_1, number_2)
        if engine.print_result(name, str(answer_correct), answer_user) is False:
            return
        i += 1
    engine.congrats(name)


if __name__ == '__main__':
    main()
