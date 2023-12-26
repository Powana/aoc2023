rows = []
with open("/home/ben/repos/AoC2023/5/input") as data:
    rows = data.readlines()
pointsum = 0

from dataclasses import dataclass

@dataclass
class NumRange:
    start: int
    len: int

class NumRange2():
    def __init__(self, start, len):
        self.start = start
        self.len = len
        

seed_paths = [int(s) for s in rows[0].split(": ")[1].split(" ")]
# seed_paths = [range(start, length) for (start, length) in  (zip(seed_paths[::2], seed_paths[1::2]))]
seed_paths = list(zip(seed_paths[::2], seed_paths[1::2]))

rows.append("\n") 
ranges = []

for row in rows[2:]:
    if row == "\n":
        new_seed_paths = []
        for i, (start_val, range_val) in enumerate(seed_paths):
            new_seed_path = [(start_val, range_val)]
            if start_val == 0:
                print("no")
            for dest_range_start, src_range_start, range_len in ranges:
                
                overlap = range(max(start_val, src_range_start), min(start_val + range_val-1, src_range_start + range_len-1)+1)
            
                if overlap:
                    new_seed_path = []
                    if overlap.start > start_val:
                        new_seed_path.append((start_val, overlap.start - start_val))

                    new_seed_path.append((dest_range_start + ( overlap.start - src_range_start ), overlap.stop-overlap.start))

                    if overlap.stop < start_val + range_val:
                        new_seed_path.append((overlap.stop, start_val+range_val-overlap.stop))
                    
                    break

                elif (start_val, range_val) not in new_seed_paths:
                    ...
                    # new_seed_path = ((start_val, range_val))
                    # new_seed_paths.append((start_val, range_val))
            new_seed_paths += new_seed_path
            
        seed_paths = new_seed_paths


        ranges = []
        print(seed_paths)
        continue
    
    if row[-2] == ":":
        print(row[:-1])
        continue

    ranges.append([int(x) for x in row.split(" ")])
    
print(min(seed_paths))


# if there is any overlap between the seed range and the dest range, translate only the overlap.
# seed 9 5 -> 9 10 11 12 13,
# map 20 10 2
# translate: 9 10 11 12 13 -> 9 20 21 12 13, what math operation is this?
# tran. rng: 10 -
# each num could be represtented by [start, range], then split when needed?


                # if 10 <= 9 <= 10 + 1 X
                # if 10 <= 9 <= 10+1 OR if 10 <= 9+5

                # if src_range_start <= start_val <= src_range_start + range_len - 1: