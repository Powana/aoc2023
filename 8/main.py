rows = []
with open("/home/ben/repos/AoC2023/8/input") as data:
    rows = data.readlines()

rl_instr = [0 if x == "L" else 1 for x in rows[0].strip()]

map = {}

for row in rows[2:]:
    print("!!", row)
    key, vals = [x.strip() for x in row.strip().split("=")]
    map[key] = tuple(vals[1:-1].split(", "))

cnt = 0
curkey = "AAA"
rl_len = len(rl_instr)
while curkey != "ZZZ":
    LR = rl_instr[cnt % rl_len]
    cnt += 1
    curkey = map[curkey][LR]

print(cnt)