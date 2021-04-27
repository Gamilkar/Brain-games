#!/usr/bin/env python
import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_question():
    sequence = ''
    l = random.randint(5, 10)
    x = random.randint(0, l-1)
    a = random.randint(1, 10)
    d = random.randint(1, 10)
    for i in range(l):
        if i == x:
            sequence += '.. '
            correct = a
        else:
            sequence += str(a) + ' '
        a += d
    return f'Question: {sequence}', correct


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    for step in range(3):
        question, correct = get_question()
        print(question)
        answer = int(input('Your answer: '))
        if answer != correct:
            print((f"'{answer}' is wrong answer ;(. Correct answer "
                   f"was '{correct}'.\nLet's try again, {name}!"))
            break
        if answer == correct:
            if step != 2:
                print('Correct!')
                continue
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
