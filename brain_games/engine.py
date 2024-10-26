import brain_games.consts as consts
import prompt


def run(game, instruction):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{instruction}')
    for i in range(consts.REPEATS):
        game_question, answer_correct = game()
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
