import prompt


def print_result(name, correct_answer, answer_user):
    if answer_user == correct_answer:
        print('Correct!')
        return True
    else:
        print("'", answer_user, "' is wrong answer ;(. Correct answer was '",
              str(correct_answer), "'", sep='')
        print("Let's try again, " + name + "!")
        return False


def welcome():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    return name


def question(*args, separator=' '):
    result = 'Question: ' + separator.join(map(str, args))
    print(result)
