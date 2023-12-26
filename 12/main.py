import numpy as np
import math
import re
import itertools

def parse_rows(rows):
    chars, nums = [], []

    for row in rows:
        r_chars, r_nums = row.strip().split(" ")
        chars.append(r_chars)
        nums.append([int(n) for n in r_nums.split(",")])
    return [chars, nums]



def part1(data):
    all_chars, all_nums = data

    arrcount_sum = 0
    for i, chars in enumerate(all_chars):
        damaged = 0
        chargroups = ["".join(grp) for num, grp in itertools.groupby(chars)]
        # d =[m for m in re.split(r'([a-z]+|[0-9]+)', chars) if m.strip()]
        # print(d)
        row_nums = all_nums[i]
        while row_nums:
            num = row_nums.pop()

        for chargroup in chargroups:
            match chargroup[0]:
                case "#":
                    damaged += len(chargroup)
                case "?":
                    if len(chargroup) < row_nums[0]:
                        pass
                    elif len(chargroup) < row_nums[0] + row_nums[1]:
                        math.comb(row_nums[0], len(chargroup))
                    ...
                case _:
                    pass



def part2(data):
    ...

if __name__ == "__main__":
    rows = []
    with open("/home/ben/repos/AoC2023/12/input") as data:
        rows = data.readlines()

    parsed_data = parse_rows(rows)
    print("Part 1:", part1(parsed_data))
    print("Part 2:", part2(parsed_data))