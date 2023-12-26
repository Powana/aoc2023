rows = []
with open("/home/ben/repos/AoC2023/1/input") as data:
    rows = data.readlines()

numstrs = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
sum = 0

for i, row in enumerate(rows):
    rownum = ""
    frow = row
    for key, val in numstrs.items():
        frow = frow.replace(key, str(val))
    
    for char in frow[:-1]:
        if char.isnumeric():
            rownum += char
        
    if len(rownum) == 1:
        rownum += rownum
    rownum = rownum[0] + rownum[-1]
    print(i, row, frow, rownum)
    sum += int(rownum)

print(sum)  # Why is 54163 not correct?