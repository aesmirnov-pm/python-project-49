#!/usr/bin/env python3


import brain_games.engine as engine
import prompt
import random


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
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        list_random_number = series_of_number()
        random_index = random.randint(1, 9)
        hidden_number = list_random_number[random_index]
        list_random_number[random_index] = ".."
        engine.question(*list_random_number)
        answer_user = prompt.string('Your answer: ')
        answer_correct = hidden_number
        if engine.print_result(name, str(answer_correct), answer_user) is False:
            return
        i += 1
    print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
