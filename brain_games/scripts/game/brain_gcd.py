#!/usr/bin/env python
import random
from brain_games.gameplay import gameplay


def main():
    information = 'Find the greatest common divisor of given numbers.'
    game_data = {}
    for step in range(3):
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 10)
        question = f'Question: {first_number} {second_number}'
        while first_number != 0 and second_number != 0:
            if first_number > second_number:
                first_number %= second_number
            else:
                second_number %= first_number
        correct = first_number + second_number
        game_data[question] = str(correct)
    gameplay(game_data, information)


if __name__ == '__main__':
    main()
