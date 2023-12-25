import os

import dotenv
import requests


def make_grid(puzzle_input):
    grid = [list(line.strip()) for line in puzzle_input]
    return grid, len(grid), len(grid[0])


def get_input(year, day):
    dotenv.load_dotenv()
    session = requests.Session()
    session.cookies.update({
        'session': os.getenv('SESSION_COOKIE')
    })
    r = session.get(f'https://adventofcode.com/{year}/day/{day}/input')
    return r.text


def write_input_to_file(year, day, filename):
    s = get_input(year, day)
    with open(filename, "w") as f:
        f.write(s)
    return s


def get_input_from_file(filename):
    return open(filename).readlines()
