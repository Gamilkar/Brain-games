#!/usr/bin/env python
from brain_games.gameplay import gameplay
from brain_games.game.gcd import get_data, INFORMATION


def main():
    gameplay(get_data, INFORMATION)


if __name__ == '__main__':
    main()
