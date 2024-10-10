#!/usr/bin/env python3


import brain_games.engine as bg
import prompt
import random


def main():
    name = bg.welcome()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        number_1 = random.randint(0, 20)
        number_2 = random.randint(0, 20)
        index = random.randint(0, 2)
        list_operator = ['+', '-', '*']
        bg.question(number_1, list_operator[index], number_2)
        answer_user = prompt.string('Your answer: ')
        expression = str(number_1) + list_operator[index] + str(number_2)
        answer_correct = eval(expression)
        if bg.print_result(name, str(answer_correct), answer_user) is False:
            return
        i += 1
    print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
