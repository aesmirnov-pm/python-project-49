#!/usr/bin/env python3


import brain_games.engine as engine
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
    name = engine.welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(1, 200)
        engine.question(number)
        print("Question: " + str(number))
        answer_user = prompt.string('Your answer: ')
        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if engine.print_result(name, correct_answer, answer_user) is False:
            return
        i += 1
    print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
