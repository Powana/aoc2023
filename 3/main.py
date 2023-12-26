rows = []
with open("/home/ben/repos/AoC2023/3/input") as data:
    rows = data.readlines()
sum = 0
int_pos = []
int_posarrs = []
int_c = ""
ints = []
rowlen = len(rows[0])-1

for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if char.isnumeric():
            int_pos.append((y, x))
            int_c += char
        else:
            if int_pos:
                int_posarrs.append( int_pos)
                ints.append(int(int_c))
            int_pos = []
            int_c = ""

gears = {}
for i, posarr in enumerate(int_posarrs):
    # print(posarr)
    top_left = max(posarr[0][0] - 1, 0), max(posarr[0][1] - 1, 0)
    top_right = max(posarr[-1][0] - 1, 0), min(posarr[-1][1] + 1, rowlen)

    bot_left = min(posarr[0][0] + 1, len(rows)-1), max(posarr[0][1] - 1, 0)
    bot_right = min(posarr[-1][0] + 1, len(rows)-1), min(posarr[-1][1] + 1, rowlen)
    print(posarr[0][0], posarr[0][1])
    print(rows[top_left[0]][top_left[1]:top_right[1]+1])
    print(rows[bot_left[0]][bot_left[1]:bot_right[1]+1])
    print(rows[posarr[0][0]][max(posarr[0][1]-1, 0)])
    print(rows[posarr[-1][0]][min(posarr[-1][1]+1, rowlen)])
    around = rows[top_left[0]][top_left[1]:top_right[1]+1] + \
             rows[bot_left[0]][bot_left[1]:bot_right[1]+1] + \
             rows[posarr[0][0]][max(posarr[0][1]-1, 0)] + \
             rows[posarr[-1][0]][min(posarr[-1][1]+1, rowlen)]
    for c in around:

        if not (c.isnumeric() or c == "." or c == "\n"):
            sum += ints[i]
            break
    
    for y in top_left[0], bot_left[0]:
        for x in range(top_left[1], top_right[1]+1):
            if rows[y][x] == "*":
                if (y, x) not in gears.keys():
                    gears[(y,x)] =  [ints[i]]
                else:
                    gears[(y,x)].append(ints[i])
    for x in max(posarr[0][1]-1, 0), min(posarr[-1][1]+1, rowlen):
        y = posarr[0][0]
        if rows[y][x] == "*":
                if (y, x) not in gears.keys():
                    gears[(y,x)] = [ints[i]]
                else:
                    gears[(y,x)].append(ints[i])
            
    """
    if not all([(c.isnumeric() or c == "." or c == "\n") for c in rows[top_left[0]][top_left[1]:top_right[1]+1]]):
        if not all([(c.isnumeric() or c == "." or c == "\n") for c in rows[bot_left[0]][bot_left[1]:bot_right[1]+1]]):
            if not all([(c.isnumeric() or c == "." or c == "\n") for c in [rows[posarr[0][0]][max(posarr[0][1]-1, 0)], rows[posarr[-1][0]][min(posarr[-1][1]+1, rowlen)]]]):
                sum += ints[i]
                print(ints[i])
    """
print(gears)
gearsum = 0
for key, val in gears.items():
    if len(val) == 2:
        gearsum += val[0]*val[1]

print("Gearsum", gearsum)
print("Sum", sum)