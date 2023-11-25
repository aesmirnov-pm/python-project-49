#!/usr/bin/env python3


import brain_games.scripts.welcome as bg
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
        number_1 = random.randint(0, 50)
        number_2 = random.randint(0, 50)
        print("Question: " + str(number_1) + " " + str(number_2))
        answer_user = prompt.string('Your answer: ')
        answer_correct = greatest_common_divisor(number_1, number_2)
        result_correct = answer_user == str(answer_correct)

        if result_correct:
            print('Correct!')
        else:
            print("'" + answer_user + "' is wrong answer ;(. Correct answer was '" + str(answer_correct) + "'")
            print("Let's try again, " + name)
            break
        i += 1
     print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
