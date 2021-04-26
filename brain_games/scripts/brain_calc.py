#!/usr/bin/env python
import prompt
import random


def get_correct(first_number, second_number, operator):
    if operator == '-':
        return first_number - second_number
    elif operator == '+':
        return first_number + second_number
    elif operator == '*':
        return first_number * second_number


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    for step in range(3):
        number_one = random.randint(0, 100)
        number_two = random.randint(0, 10)
        operator = random.choice(['+', '-', '*'])
        correct = get_correct(number_one, number_two, operator)
        print(f'Question: {number_one} {operator} {number_two}')
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
