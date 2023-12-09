#!/usr/bin/env python3


import brain_games.engine as bg
import prompt
import random


def greatest_common_divisor(number_1, number_2):
    min_number = min(number_1, number_2)
    max_number = max(number_1, number_2)
    while max_number % min_number != 0:
        max_number, min_number = min_number, max_number % min_number
    return min_number


def main():
    name = bg.welcome()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        number_1 = random.randint(2, 50)
        number_2 = random.randint(2, 50)
        print("Question: " + str(number_1) + " " + str(number_2))
        answer_user = prompt.string('Your answer: ')
        answer_correct = greatest_common_divisor(number_1, number_2)
        if bg.print_result(name, str(answer_correct), answer_user) is False:
            return
        i += 1
    print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
