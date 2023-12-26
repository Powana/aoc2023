from math import lcm
rows = []
with open("/home/ben/repos/AoC2023/8/input") as data:
    rows = data.readlines()

rl_instr = [0 if x == "L" else 1 for x in rows[0].strip()]

map = {}

for row in rows[2:]:
    key, vals = [x.strip() for x in row.strip().split("=")]
    map[key] = tuple(vals[1:-1].split(", "))

curkeys = []
cnts = []
cntsmul = 1
for k in map.keys():
    if k[-1] == "A":
        curkeys.append(k)

rl_len = len(rl_instr)

for curkey in curkeys:
    cnt = 0
    while curkey[-1] != "Z":

        LR = rl_instr[cnt % rl_len]
        cnt += 1
        curkey = map[curkey][LR]
        # print(curkey)
        # print(" ".join(k[-1] for k in curkeys))
        
    cnts.append(cnt)

print(lcm(*cnts))