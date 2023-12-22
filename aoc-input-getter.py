# get the input of a given year and day from advent of code
# usage: python aoc-input-getter.py <year> <day>
# example: python aoc-input-getter.py 2015 15
# example: python aoc-input-getter.py 2018 1
import os

import dotenv
import sys

import requests


def get_input(year, day):
    dotenv.load_dotenv()
    session = requests.Session()
    session.cookies.update({
        'session': os.getenv('SESSION_COOKIE')
    })
    r = session.get(f'https://adventofcode.com/{year}/day/{day}/input')
    return r.text


def main():
    year = sys.argv[1]
    day = sys.argv[2]
    s = get_input(year, day)
    # put input in "input.txt"
    with open("input.txt", "w") as f:
        f.write(s)


if __name__ == '__main__':
    main()
