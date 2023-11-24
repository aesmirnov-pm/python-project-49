#!/usr/bin/env python3


import brain_games.scripts.welcome as bg
import prompt
import random


def main():
    name = bg.main()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        number_1 = random.randint(0, 20)
        number_2 = random.randint(0, 20)
        index = random.randint(0, 2)
        list_operator = ['+', '-', '*']
        print("Question: " + str(number_1) + " " + list_operator[index] + " " + str(number_2))
        answer_user = prompt.string('Your answer: ')
        answer_correct = eval(str(number_1) + list_operator[index] + str(number_2))
        result_correct = answer_user == str(answer_correct)

        if result_correct:
            print('Correct!')
        else:
            print("'" + answer_user + "' is wrong answer ;(. Correct answer was '" + str(answer_correct) + "'")
            print("Let's try again, " + name)
            break
        i += 1


if __name__ == '__main__':
    main()
