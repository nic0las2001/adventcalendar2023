input = open("d7.txt","r")

part = 1

combination = {1:[],2:[],"tp":[],3:[],"f":[],4:[],5:[]}


for line in input:
    hand = line.split()
    hand_dict = {}
    for char in hand[0]:
        if char not in hand_dict:
            hand_dict[char] = 1
        else:
            hand_dict[char] +=1

    if "J" in hand_dict.keys() and part == 2:
        j_val = hand_dict["J"]
        if j_val != 5:
            del hand_dict["J"]
        for key,val in hand_dict.items():
            if key != "J" and val == max(hand_dict.values()):
                hand_dict[key] += j_val
                break

    if max(hand_dict.values()) == 3 and min(hand_dict.values()) == 2:
        combination["f"].append((hand[0],hand_dict,hand[1]))
    elif sorted(hand_dict.values()) == sorted([2,2,1]):
        combination["tp"].append((hand[0],hand_dict,hand[1]))
    else:
        combination[max(hand_dict.values())].append((hand[0],hand_dict,hand[1]))

match part:
    case 1:
        order = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}
    case 2:
        order = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}
for key in combination:
    combination[key].sort(key=lambda x: tuple(order[i] for i in x[0]))

rank = 1
tot_sum = 0
for key,val in combination.items():
    for item in combination[key]:
        score = rank*int(item[2])
        tot_sum+= score
        rank += 1

print(tot_sum)