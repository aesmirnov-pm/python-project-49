#!/usr/bin/env python3


import brain_games.scripts.welcome as bg
import prompt
import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    name = bg.main()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(1, 200)
        print("Question: " + str(number))
        answer_user = prompt.string('Your answer: ')
        if is_prime(number):
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
