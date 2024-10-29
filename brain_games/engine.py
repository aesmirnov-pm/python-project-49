from brain_games.consts import REPEATS
import prompt


def run(game, instruction):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{instruction}')
    for i in range(REPEATS):
        game_question, answer_correct = game()
        print(f'Question: {game_question}')
        answer_user = prompt.string('Your answer: ')
        if answer_user == str(answer_correct):
            print('Correct!')
        else:
            print(
                f"'{answer_user}' is wrong answer ;(."
                f"Correct answer was '{answer_correct}'\n"
                f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
