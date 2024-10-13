#!/usr/bin/env python3


import brain_games.engine as engine
import prompt
import random
import brain_games.consts as consts


def series_of_number():
    series_of_number = []
    random_number = random.randint(2, 15)
    step = random.randint(2, 5)
    while len(series_of_number) <= 10:
        series_of_number.append(random_number)
        random_number = random_number + step
    return series_of_number


def main():
    name = engine.welcome()
    print(consts.PROGRESSION_INSTRUCTION)
    i = 0
    while i < consts.REPEATS:
        list_random_number = series_of_number()
        random_index = random.randint(1, 9)
        hidden_number = list_random_number[random_index]
        list_random_number[random_index] = ".."
        engine.question(*list_random_number)
        answer_user = prompt.string(consts.YOUR_ANSWER)
        answer_correct = hidden_number
        if engine.print_result(name, str(answer_correct), answer_user) is False:
            return
        i += 1
    engine.congrats(name)


if __name__ == '__main__':
    main()
