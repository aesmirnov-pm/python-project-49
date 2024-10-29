import prompt


def welcome():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f"Hello, {name}")
    return name
