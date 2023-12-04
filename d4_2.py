input = open("d4.txt","r")
line_list = input.readlines()

def format_func(card):
    card = card.replace(":"," |")
    card = card.replace("\n","")
    card = card.split(" | ")

    return card

score = 0
i = 0
dupe_dict = {}
card_count = {}
while i < len(line_list):
    card_count[i] = 1
    line = line_list[i]
    card = format_func(line)
    user_num = card[1].split()
    win_num = card[2].split()

    line_score = 0
    li = 0
    dupe_dict[i] = []
    for num in user_num:
        if num in win_num:
            li += 1
            dupe_dict[i].append(i+li)
    i += 1

for key,val in dupe_dict.items():
    for count in val:
        card_count[count] += 1*card_count[key]

print("Part 2: ", sum(card_count.values()))
