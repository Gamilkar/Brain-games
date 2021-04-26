#!/usr/bin/env python
import prompt
import random


def get_correct(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for step in range(3):
        number = random.randint(0, 1000)
        correct = get_correct(number)
        print(f'Question: {number}')
        answer = input('Your answer: ')
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
