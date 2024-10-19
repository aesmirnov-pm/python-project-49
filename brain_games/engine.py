

import brain_games.cli as cli
import brain_games.consts as consts
import prompt


def run(game):
    name = cli.welcome()
    print(game.INSTRUCTION)
    for i in range(consts.REPEATS):
        game_question, answer_correct = game.return_question_and_answer()
        print(game_question)
        answer_user = prompt.string('Your answer: ')
        if print_result(name, str(answer_correct), answer_user) is False:
            return
    congrats(name)


def print_result(name, correct_answer, answer_user):
    if answer_user == correct_answer:
        print('Correct!')
        return True
    else:
        print("'", answer_user, "' is wrong answer ;(. Correct answer was '",
              str(correct_answer), "'", sep='')
        print("Let's try again, " + name + "!")
        return False


def question(*args, separator=' '):
    return 'Question: ' + separator.join(map(str, args))


def congrats(name):
    print("Congratulations, " + name + "!")
