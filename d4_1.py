input = open("d4.txt","r")

score = 0
for line in input:
    card = line
    card = card.replace(":"," |")
    card = card.replace("\n","")
    card = card.split(" | ")
    
    user_num = card[1].split()
    win_num = card[2].split()
    
    line_score = 0
    for num in user_num:
        if num in win_num:
            line_score = max([2*line_score,1])
    score += line_score

print("Part 1: ", score)
