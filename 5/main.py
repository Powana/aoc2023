rows = []
with open("/home/ben/repos/AoC2023/5/input") as data:
    rows = data.readlines()
pointsum = 0

og_seeds = [int(s) for s in rows[0].split(": ")[1].split(" ")]
seed_paths = og_seeds.copy()
rows.append("\n") 
ranges = []

for row in rows[2:]:
    if row == "\n":
        for i, translated_value in enumerate(seed_paths):
            for dest_range_start, src_range_start, range_len in ranges:
                if src_range_start <= translated_value <= src_range_start + range_len - 1:
                    seed_paths[i] = dest_range_start + translated_value - src_range_start
                    break

        ranges = []
        print(seed_paths)
        continue
    
    if row[-2] == ":":
        continue

    ranges.append([int(x) for x in row.split(" ")])
    
print(min(seed_paths))