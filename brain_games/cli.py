import prompt


def welcome():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print("Hello, " + name)
    return name
