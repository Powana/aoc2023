from collections import Counter
from functools import cmp_to_key
rows = []
with open("/home/ben/repos/AoC2023/7/input") as data:
    rows = data.readlines()
s = 0

vals = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}# part 2, J: 11 -> 1

hands = []
bids = []

for row in rows:
    hand, bid = row.split(" ")
    hands.append(hand)
    bids.append(int(bid))

hands_bids = dict(zip(hands, bids))

    

    
def compare_hands(hand_a, hand_b):
    worth_a, worth_b = get_worth(hand_a), get_worth(hand_b)
    if worth_a > worth_b:
        return -1
    elif worth_a < worth_b:
        return 1
    
    for i, c in enumerate(hand_a):
        if vals[c] > vals[hand_b[i]]:
            return -1
        elif vals[c] < vals[hand_b[i]]:
            return 1
    
    return 0
        
    raise IndexError("YOUVE GONE TOO FAR THIS TIME.")

def get_worth(hand: str):
    worth = 0  # 0 = high card, 6 = five of a kind
    valcounts = Counter(hand)
    sorted_vals = sorted(valcounts.keys(), key=lambda x: valcounts[x], reverse=True)
    if sorted_vals[0] != "J":
        hand = hand.replace("J", sorted_vals[0])
    elif hand != "JJJJJ":
        hand = hand.replace("J", sorted_vals[1])
    
    valcounts = Counter(hand)
    sorted_valcounts = sorted(valcounts.values(), reverse=True)

    match sorted_valcounts[0]:
        case 5:
            worth = 6
        case 4:
            worth = 5
        case 3:
            if sorted_valcounts[1] == 2:
                worth = 4
            else:
                worth = 3
        case 2:
            if sorted_valcounts[1] == 2:
                worth = 2
            else:
                worth = 1
        case _:
            worth = 0
    
    return worth


sorted_hands = sorted(hands, key=cmp_to_key(compare_hands), reverse=True)

print(sorted_hands)

for i, hand in enumerate(sorted_hands):
    s += hands_bids[hand] * (i+1)


print(s)