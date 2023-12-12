import numpy as np
import sys
sys.setrecursionlimit(100000)

input = open("d10.txt","r")

def path_finding(coordinates, previous, maze):
    count = 1
    i,j = coordinates

    s_flag = True
    char = maze[i][j]
    s_check = (char == "S")

    # top bttm left right 
    av_dict = {"L":[1,0,0,1],"F":[0,1,0,1],"J":[1,0,1,0],"7":[0,1,1,0],"S":[1,1,1,1],"-":[0,0,1,1],"|":[1,1,0,0]}
    available = av_dict[maze[i][j]]

    # Top
    if (i-1,j) != previous and available[0] and s_flag:
        if maze[i-1][j] in "F|7":
            count += path_finding((i-1,j), coordinates, maze)
            if s_check:
                s_flag = False
        elif  maze[i-1][j] == "S":
            return count

    # Bttm
    if (i+1,j) != previous and available[1] and s_flag:
        if maze[i+1][j] in "L|J":
            count += path_finding((i+1,j), coordinates, maze) 
            if s_check:
                s_flag = False
        elif  maze[i+1][j] == "S":
            return count

    # Left
    if (i,j-1) != previous and available[2] and s_flag:
        if maze[i][j-1] in "-FL":
            count += path_finding((i,j-1), coordinates, maze) 
            if s_check:
                s_flag = False
        elif  maze[i][j-1] == "S":
            return count
    
    # Right
    if (i,j+1) != previous and available[3] and s_flag:
        if maze[i][j+1] in "-J7":
            count += path_finding((i,j+1), coordinates, maze)
            if s_check:
                s_flag = False
        elif  maze[i][j+1] == "S":
            return count
                
    return count


# Convert maze into iterable array 
maze = []
for line in input:
    data = list(line)
    maze.append(data)

# Find starting point of pipe maze
i = 0
for sublist in maze:
    if "S" in sublist:
        j = sublist.index("S")
        break 
    i += 1
start = (i,j)

count = path_finding(start, start, maze) 
print(int(count/2))


