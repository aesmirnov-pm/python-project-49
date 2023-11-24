#!/usr/bin/env python3


import brain_games.scripts.welcome as bg
import prompt
import random


def main():
    name = bg.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        c = random.randint(0, 20)
        print("Question: " + str(c))
        answer_user = prompt.string('Your answer: ')
        is_even = c % 2 == 0
        if is_even:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        result = answer_user == correct_answer
        if result:
            print('Correct!')
        else:
            print("'" + answer_user + "' is wrong answer ;(. Correct answer was '" + correct_answer + "'")
            print("Let's try again, " + name)
            break
        i += 1


if __name__ == '__main__':
    main()
