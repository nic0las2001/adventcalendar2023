from math import lcm
input = open("d8.txt","r")

skip = True
instructions=""
nodes = {}

# Read input and match directions to tuples 
for line in input:
    if skip:
        instructions = line[0:-1]
        skip = False
    elif line[0].isalpha():
        node = line.split(" = ")
        nodes[node[0]] = (node[1][1:4],node[1][6:9])

def path_finder(instructions, nodes, start, part):
    current = start
    dir_dict = {'L':0,"R":1}
    count = 0
    i = 0
    while True:
        if i < len(instructions):
            matches = nodes[current]
            current = matches[dir_dict[instructions[i]]]
            count += 1
            i += 1 
            if (current.endswith("Z") and part == 2) or (part == 1 and current == "ZZZ"):
                break
            elif i == len(instructions):
                i = 0
    return count


# Part 1
part = 1
print("P1: ",path_finder(instructions, nodes,"AAA",part))

# Part 2
part = 2
start_list = []
for key in nodes.keys():
    if key[-1] == "A":
        start_list.append(key)

final = 1
# Use least common multiplier for each starting value
# Path is cyclical and repeats eventually, so calculate how long it takes for each
# to reach a Z and compute an LCM of that
for value in start_list:
    final = lcm(final, path_finder(instructions, nodes,value,part))
print("P2: ",final)
