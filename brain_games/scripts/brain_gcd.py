#!/usr/bin/env python
import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_correct(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    return first_number + second_number

def main():
    
    name = welcome_user()

    print('Find the greatest common divisor of given numbers.')
    
    for step in range(3):
        number_one = random.randint(1, 100)
        number_two = random.randint(1, 10)

        correct = get_correct(number_one, number_two)

        print(f'Question: {number_one} {number_two}')
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
