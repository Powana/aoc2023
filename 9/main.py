rows = []
with open("/home/ben/repos/AoC2023/9/input") as data:
    rows = data.readlines()
s = 0

def get_deltas(iter):
    r = []
    for i, x in enumerate(iter[1:], 1):
        r.append(x - iter[i-1])
    return r

di = 0
for row in rows:
    vals = [int(x) for x in row.split(" ")][::-1]
    all_deltas = [vals]

    deltas = get_deltas(vals)
    
    while not all(x == 0 for x in deltas):  # while sum(deltas) != 0:  ## GDI, this doesnt work bcuzz of neg nums
        all_deltas.append(deltas)
        deltas = get_deltas(deltas)
        print(di, deltas)
    print(di, deltas)
    all_deltas.append(deltas)
    
    len_all_deltas = len(all_deltas)
    for i in range(1, len_all_deltas): # numerate(all_deltas[::-1], start=1):
        real_i = len_all_deltas - i - 1
        all_deltas[real_i].append(all_deltas[real_i][-1] + all_deltas[real_i + 1][-1])
    print("i:", di, all_deltas[0][-1])
    s += all_deltas[0][-1]
    di += 1

print(s)
    