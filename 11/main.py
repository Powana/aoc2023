import numpy as np
import itertools

def parse_rows(rows):
    d = np.array([list(row.strip()) for row in rows])
    
    j = 0
    for i, row in enumerate(d):
        if np.all(row == "."):
            d = np.insert(d, i+j, row, axis=0)
            j += 1
    d = np.rot90(d)

    j = 0
    for i, row in enumerate(d):
        if np.all(row == "."):
            d = np.insert(d, i+j, row, axis=0)
            j+= 1
    d = np.rot90(d, 3)
    return d

def parse_rows2(rows):
    d = np.array([list(row.strip()) for row in rows])
    
    big_rows, big_cols = [], []
    for i, row in enumerate(d):
        if np.all(row == "."):
            big_rows.append(i)
    d = np.rot90(d, -1)

    for i, row in enumerate(d):
        if np.all(row == "."):
            big_cols.append(i)
    d = np.rot90(d, 1)
    return d, big_cols, big_rows

    
def part1(data):
    lengths = 0

    galaxies = np.array(list(zip(*np.where(data == "#"))))

    for yx1 in galaxies:
        for yx2 in galaxies:
            if not np.all(yx1 == yx2):
                lengths += abs(yx1[0]-yx2[0]) + abs(yx1[1]-yx2[1])
                # print(yx1, yx2, lengths[-1])
    
    return lengths//2

def part2(rows):
    lengths = 0
    data, big_cols, big_rows = parse_rows2(rows)
    print("bc", big_cols)
    print("br", big_rows)

    galaxies = np.array(list(zip(*np.where(data == "#"))))

    for yx1 in galaxies:
        for yx2 in galaxies:
            if not np.all(yx1 == yx2):
                sort_y = [yx1[0], yx2[0]]
                sort_y.sort()
                sort_x = [yx1[1], yx2[1]]
                sort_x.sort()
                added_millions = 0
                for big_col in big_cols:
                    if big_col in range(sort_x[0]+1, sort_x[1]):
                        added_millions += 1
                for big_row in big_rows:
                    if big_row in range(sort_y[0]+1, sort_y[1]):
                        added_millions += 1
                
                lengths += sort_y[1]-sort_y[0] + sort_x[1]-sort_x[0] + added_millions*1_000_000- added_millions #21 diff on ez
    return lengths//2

if __name__ == "__main__":
    rows = []
    with open("/home/ben/repos/AoC2023/11/input") as data:
        rows = data.readlines()

    #parsed_data = parse_rows(rows)
    #print("Part 1:", part1(parsed_data))
    print("Part 2:", part2(rows))