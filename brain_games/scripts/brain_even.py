#!/usr/bin/env python
import prompt
import random

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        number = random.randint(0, 1000)
        print(f'Question: {number}')
        answer = input('Your answer: ')
        check = ''
        if number % 2 == 0:
            check = 'yes'
        elif number % 2 != 0:
            check = 'no'
        if answer == check:
            if i == 2:
                print(f'Congratulations, {name}!')
            else:
                print('Correct!')
            continue
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{check}".')
            print(f"Let's try again, {name}!")
            break


if __name__ == '__main__':
    main()