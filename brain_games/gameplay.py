import prompt


def gameplay(game_data, information):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(information)
    for level, question in enumerate(game_data):
        print(question)
        correct = game_data[question]
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
