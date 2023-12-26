import numpy as np
import re
import math

rows = []
with open("/home/ben/repos/AoC2023/6/input") as data:
    rows = data.readlines()
s = 1
 
durations = [int(x) for x in re.split('\s{2,}', rows[0].strip())[1:]]
records = [int(x) for x in re.split('\s{2,}', rows[1].strip())[1:]]

big_duration = int("".join(str(x) for x in durations))
big_record = int("".join(str(x) for x in records))

def get_length(button_hold_ms, race_duration):
    return (race_duration-button_hold_ms) * button_hold_ms

def bhms(record, race_dur):
    y = race_dur
    z = record
    x1 = -((-y+math.sqrt(pow(y, 2) - 4*z))/2)
    x2 = -((-y-math.sqrt(pow(y, 2) - 4*z))/2)
    return math.ceil(x1), math.floor(x2)


for (duration, record) in zip(durations, records):
    bhms1, bhms2 = bhms(record+1, duration)
    # print("Record", record, "Duration", duration)
    # print(bhms1, bhms2, math.ceil(bhms2)-math.floor(bhms1)+1)
    s *= bhms2 - bhms1+1

bhms1, bhms2 = bhms(big_record+1, big_duration)
# print("Record", record, "Duration", duration)
# print(bhms1, bhms2, math.ceil(bhms2)-math.floor(bhms1)+1)
big_sum = bhms2 - bhms1+1

print(big_sum)



print(s)