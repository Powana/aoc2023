def parse_rows(rows):
    return rows


def part1(data):
    ...


def part2(data):
    ...

if __name__ == "__main__":
    rows = []
    with open("/home/ben/repos/AoC2023/10/input") as data:
        rows = data.readlines()

    parsed_data = parse_rows(rows)
    print("Part 1:", part1(parsed_data))
    print("Part 2:", part2(parsed_data))