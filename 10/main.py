import numpy as np
from itertools import chain
from typing import *

# char : connectivity [N,E,S,W]
# char : [y_delta, x_delta]
# char : ([y_delta, x_delta], (y_delta, x_delta)) (first when coming from the first clockwise direction from the top, then the opposite)
pipe_map = {"-":((0, -1), (0, 1)), "|": ((1, 0), (-1, 0)), "F": ((1, 0), (0, 1)), "7":((0, -1), (1, 0)), "J": ((0, -1), (-1, 0)), "L": ((0, 1), (-1, 0))}
pipe_chain = []

def follow(data, y, x):
    pipe_char = data[y, x]
    pipe_chain.append(((y, x)))
    yx_deltas_1, yx_deltas_2 = pipe_map[pipe_char]
    next_y, next_x = y + yx_deltas_1[0], x + yx_deltas_1[1]
    if pipe_chain[-2] == (next_y, next_x):  # check that the direction we picked is not going back to where we were, bit of a hack but fast and works
        next_y, next_x = y + yx_deltas_2[0], x + yx_deltas_2[1]
    
    # pipe_chain.append((next_y, next_x))
    return next_y, next_x


def parse_rows(rows):
    # return np.array([np.fromstring(row.split()) for row in rows])
    return np.array([list(row.strip()) for row in rows])

def common(data):
    start_y, start_x = [x[0] for x in np.where(data == "S")]
    # surrounding = data[start_y-1:start_y+2, start_x-1:start_x+2]
    # print(surrounding)
    # for tile in surrounding:
    #     pass
    start_char = "F"#"7"  # done manually, could/should ofc be done better
    data[start_y, start_x] = start_char

    pipe_chain.append((start_y, start_x))
    next_y, next_x = follow(data, start_y, start_x)

    while (next_y != start_y) or (next_x != start_x):
        next_y, next_x = follow(data, next_y, next_x)
    

def get_in_out_regions(data):
    outsides = []
    insides = []

    ground = np.where(data == ".")
    ground_coords = np.array(list(zip(*ground)))
    ymax, xmax = data.shape[0]-1, data.shape[1]-1

    visited = []
    ground_regions = []

    # brute force approach
    for og_y, og_x in ground_coords:
        if (og_y, og_x) in visited:
            continue
        ground_region = [(og_y,og_x)]
        visited.append((og_y, og_x))

        
        #if y == 0 or y == big_clean_data.shape[0]-1 or x == 0 or x == big_clean_data.shape[1]-1:
        #    outsides.append((y, x))
        #    continue
        #    ...

        to_visit = [(og_y, og_x)]
        while to_visit:
            y, x = to_visit.pop()
            visited.append((y, x))
            # print("To visit:", y, x)
            
            adj_coords = [(max(y-1, 0),x), (y,min(x+1, xmax)), (min(y+1, ymax),x), (y,max(x-1, 0))]

            for ny, nx in adj_coords:
                visited.append((y,x))
                if data[ny, nx] == ".":
                    if ((ny, nx)) not in ground_region:
                        ground_region.append((ny, nx))
                        to_visit.append((ny,nx))
                    continue
        ground_regions.append(ground_region)

        #nesw_surrounding = big_clean_data[y-1,x], big_clean_data[y,x+1], big_clean_data[y+1,x], big_clean_data[y,x-1]
        #nexts = np.where(np.array(nesw_surrounding) == ".")
        #print(nesw_surrounding)
        #print(nexts)
        # if "." in (n,e,s,w):
    
    for region in ground_regions:
        out = False
        for y, x in region:
            if y == 0 or y == data.shape[0]-1 or x == 0 or x == data.shape[1]-1:
                outsides.append(region)
                out = True
                break
        if not out:
            insides.append(region)
    
    return insides, outsides
    



def part1(data: List[List[str]]):
    common(data)

    return(len(pipe_chain)//2)


def part2(data):
    common(data)

    # possible approaches:
        # double the size of data, inserting either a . or a pipe between each tile, to easier determine if a . can reach the outside of the loop
    # figured out later: find the ground on small scale, then sample on large scale to see if they touch the outside
    print(1)

    cleaned_data = np.full(data.shape, ".")
    for y, x in pipe_chain:
        cleaned_data[y, x] = data[y, x]  # prob a faster way to do this with np
    
    big_clean_data = np.full((data.shape[0]*2, data.shape[1]*2), ".")
    for i, (y, x) in enumerate(pipe_chain):
        big_clean_data[y*2, x*2] = data[y, x]  # prob a faster way to do this with np
        if i == 0:
            delta_y, delta_x = y - pipe_chain[-1][0], x - pipe_chain[-1][1]

        delta_y, delta_x = y - pipe_chain[i-1][0], x - pipe_chain[i-1][1]
        if delta_y:
            big_clean_data[y*2 - delta_y, x*2] = "|"
        elif delta_x:
            big_clean_data[y*2, x*2 - delta_x] = "-"
    print(2)  

    small_insides, small_outsides = get_in_out_regions(cleaned_data)

    print(3)
    big_insides, big_outsides = get_in_out_regions(big_clean_data)
    small_insides_forrealthistime = []
    print(4)

    for row in big_clean_data:
        print("".join(row))

    big_insides_flat = list(chain.from_iterable(big_insides))

    for region in small_insides:
        for (y, x) in region:
            if (y*2, x*2) in big_insides_flat:
                small_insides_forrealthistime.append((y,x))
                print("Inside acquired")
    

    rows, cols = [c[0] for c in small_insides_forrealthistime], [c[1] for c in small_insides_forrealthistime]
    cleaned_data[rows, cols] = "I"
        
    
    for row in cleaned_data:
        print("".join(row))

    print(len(small_insides))

    return len(small_insides_forrealthistime)


if __name__ == "__main__":
    rows = []
    with open("/home/ben/repos/AoC2023/10/input") as data:
        rows = data.readlines()

    parsed_data = parse_rows(rows)
    # print("Part 1:", part1(parsed_data))
    print("Part 2:", part2(parsed_data))