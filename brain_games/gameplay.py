import prompt


def gameplay(function, information):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(information)
    for level in range(3):
        (question, correct) = function()
        print(question)
        answer = input('Your answer: ')
        if answer != correct:
            print((f"'{answer}' is wrong answer ;(. Correct answer "
                   f"was '{correct}'.\nLet's try again, {name}!"))
            break
        if answer == correct:
            if level != 2:
                print('Correct!')
                continue
            print(f'Congratulations, {name}!')
