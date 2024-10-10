#!/usr/bin/env python3


import brain_games.engine as bg
import prompt
import random


def main():
    name = bg.welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_num = random.randint(0, 20)
        bg.question(random_num)
        answer_user = prompt.string('Your answer: ')
        is_even = c % 2 == 0
        if is_even:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if bg.print_result(name, correct_answer, answer_user) is False:
            return
        i += 1
    print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
