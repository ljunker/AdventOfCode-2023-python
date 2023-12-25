# get the input of a given year and day from advent of code
# usage: python aoc-input.py <year> <day>
# example: python aoc-input.py 2015 15
# example: python aoc-input.py 2018 1




def main():
    year = sys.argv[1]
    day = sys.argv[2]
    s = get_input(year, day)
    # put input in "input.txt"
    with open("input.txt", "w") as f:
        f.write(s)


if __name__ == '__main__':
    main()
