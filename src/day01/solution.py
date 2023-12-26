from typing import Final


def first_and_last_digit(input: str) -> int:
    first_digit = "\0"
    for c in input:
        if c.isdigit():
            first_digit = c
            break

    last_digit = "\0"
    for i in range(len(input) - 1, -1, -1):
        if input[i].isdigit():
            last_digit = input[i]
            break

    return int(first_digit + last_digit)


def solve1(input: str) -> int:
    sum = 0
    for line in input.splitlines():
        sum += first_and_last_digit(line)

    return sum


NUM_BY_WORD: Final = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def to_num(x: str) -> int:
    if x in NUM_BY_WORD:
        return NUM_BY_WORD[x]
    else:
        return int(x)


def first_and_last_number(input: str) -> int:
    nums = []
    for i, c in enumerate(input):
        if c.isdigit():
            nums.append((i, c))

    for word in NUM_BY_WORD:
        i = input.find(word)
        if i != -1:
            nums.append((i, word))

    nums.sort(key=lambda p: p[0])

    rnums = []
    for i in range(len(input) - 1, -1, -1):
        if input[i].isdigit():
            rnums.append((i, input[i]))

    for word in NUM_BY_WORD:
        i = input.rfind(word)
        if i != -1:
            rnums.append((i, word))

    rnums.sort(key=lambda p: p[0], reverse=True)

    first = to_num(nums[0][1])
    last = to_num(rnums[0][1])

    return first * 10 + last


def solve2(input: str) -> int:
    sum = 0
    for line in input.splitlines():
        sum += first_and_last_number(line)

    return sum
