import numpy as np

a = [[1,1,1,1], [0,2,0,0], [0,2,0,0], [0,2,0,0]]
na = np.array(a)

na = np.insert(na, 1, [2,2,2,2], axis=0)
print(na)
b = np.rot90(na, -1)
print(b)
# print(na.shape[0]*2, na.shape[1]*2)

b = [1,2,3,4,5,6,7,8,9]
pairs = []
for el in b:
    for el2 in b:
        if (el2 != el) and (el2, el) not in pairs:
            pairs.append((el, el2))
