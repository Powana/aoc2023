rows = []
with open("/home/ben/repos/AoC2023/4/input") as data:
    rows = data.readlines()
pointsum = 0


copies = [1,]*len(rows)
for i, row in enumerate(rows):
    _, nums = row.split(":")
    
    own_nums, win_nums = [[(int(c) if c != "" else None) for c in x.strip().split(" ") if c] for x in nums.split("|")]
    matches = 0

    for n in win_nums:
        if n in own_nums:
            matches += 1
    
    if matches:
        pointsum += pow(2, matches-1)
        
        # copies[i:i+matches] += copies[i]
        for ii in range(i+1, i+matches+1):
            copies[ii] += copies[i]

print(pointsum)
print(sum(copies))