from Timer import timer

data = open('input.txt', 'r').read()


def find_calib_value(line):
    digits = [char for char in line if char.isdigit()]
    return int(digits[0] + digits[-1])


@timer
def part1():
    lines = data.split('\n')
    print(sum([find_calib_value(line) for line in lines]))


def convert_to_digit(word):
    word_to_digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    return word_to_digit.get(word, '')


def find_calib_value2(line):
    digits_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = []

    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(line[i])
        if line[i].isalpha():
            for digit in digits_words:
                if line[i:i + len(digit)] == digit:
                    digits.append(convert_to_digit(digit))
    return int(digits[0] + digits[-1])


@timer
def part2():
    lines = data.split('\n')
    print(sum([find_calib_value2(line) for line in lines]))


part1()
part2()
print("Done")
