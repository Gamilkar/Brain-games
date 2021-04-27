#!/usr/bin/env python
import random
from brain_games.gameplay import gameplay


def main():
    information = 'What is the result of the expression?'
    game_data = {}
    for i in range(3):
        first_number = random.randint(0, 100)
        second_number = random.randint(0, 10)
        operator = random.choice(['+', '-', '*'])
        question = f'Question: {first_number} {operator} {second_number}'
        if operator == '-':
            correct = first_number - second_number
        elif operator == '+':
            correct = first_number + second_number
        elif operator == '*':
            correct = first_number * second_number
        game_data[question] = str(correct)
    gameplay(game_data, information)


if __name__ == '__main__':
    main()
