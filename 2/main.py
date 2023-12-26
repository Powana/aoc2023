rows = []
with open("/home/ben/repos/AoC2023/2/input") as data:
    rows = data.readlines()
sum = 0
"""
maxs = {"red": 12, "green": 13, "blue": 14}

for row in rows:
    row = row[:-1]
    invalid = False
    id = int(row.split(":")[0][5:])
    subsets = row.split(":")[1].split(";")
    for subset in subsets:
        colours = subset.split(",")
        for colour in colours:
            print(colour.split(" "))
            [_, cval, cname] = colour.split(" ")
            if int(cval) > maxs[cname]:
                invalid = True
    if not invalid:
        sum += id

print(sum)
"""

for row in rows:
    row = row[:-1]
    colourmins = {"red": 0, "green": 0, "blue": 0}
    # id = int(row.split(":")[0][5:])
    subsets = row.split(":")[1].split(";")
    for subset in subsets:
        colours = subset.split(",")
        for colour in colours:
            print(colour.split(" "))
            [_, cval, cname] = colour.split(" ")
            colourmins[cname] = max(colourmins[cname], int(cval))

    sum += colourmins["red"] * colourmins["green"] * colourmins["blue"]

print(sum)