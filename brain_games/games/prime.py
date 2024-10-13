#!/usr/bin/env python3


import brain_games.engine as engine
import prompt
import random
import brain_games.consts as consts


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    name = engine.welcome()
    print(consts.PRIME_INSTRUCTION)
    i = 0
    while i < consts.REPEATS:
        number = random.randint(1, 200)
        engine.question(number)
        print("Question: " + str(number))
        answer_user = prompt.string(consts.YOUR_ANSWER)
        if is_prime(number):
            correct_answer = consts.YES
        else:
            correct_answer = consts.NO
        if engine.print_result(name, correct_answer, answer_user) is False:
            return
        i += 1
    engine.congrats(name)


if __name__ == '__main__':
    main()
