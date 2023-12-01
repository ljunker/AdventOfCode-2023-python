from Timer import timer

data = open('input.txt', 'r').read()


def find_calib_value(line):
    digits = [char for char in line if char.isdigit()]
    if len(digits) >= 2:
        first = digits[0]
        last = digits[-1]
        return int(first + last)
    if len(digits) == 1:
        return int(digits[0] + digits[0])
    return 0


@timer
def part1():
    total_sum = 0
    lines = data.split('\n')
    for line in lines:
        calib_value = find_calib_value(line)
        if calib_value != 0:
            total_sum += calib_value
    print(total_sum)


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
    if len(digits) >= 2:
        first = digits[0]
        last = digits[-1]
        return int(first + last)
    if len(digits) == 1:
        return int(digits[0] + digits[0])
    return 0


@timer
def part2():
    total_sum = 0
    lines = data.split('\n')
    for line in lines:
        calib_value = find_calib_value2(line)
        if calib_value != 0:
            total_sum += calib_value
    print(total_sum)


part1()
part2()
print("Done")
