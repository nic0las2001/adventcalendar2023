import numpy as np
import sys
sys.setrecursionlimit(100000)

input = open("d10.txt","r")

def path_finding(coordinates, previous, maze, visited):
    visited.append(coordinates)

    i,j = coordinates
    # print(maze[i][j])

    s_flag = True
    char = maze[i][j]
    s_check = (char == "S")

    # top bttm left right 
    av_dict = {"L":[1,0,0,1],"F":[0,1,0,1],"J":[1,0,1,0],"7":[0,1,1,0],"S":[1,1,1,1],"-":[0,0,1,1],"|":[1,1,0,0]}
    available = av_dict[maze[i][j]]

    # Top
    if (i-1,j) != previous and available[0] and s_flag:
        if maze[i-1][j] in "F|7":
            visited = path_finding((i-1,j), coordinates, maze, visited)
            if s_check:
                s_flag = False
        elif  maze[i-1][j] == "S":
            return visited

    # Bttm
    if (i+1,j) != previous and available[1] and s_flag:
        if maze[i+1][j] in "L|J":
            visited = path_finding((i+1,j), coordinates, maze, visited) 
            if s_check:
                s_flag = False
        elif  maze[i+1][j] == "S":
            return visited

    # Left
    if (i,j-1) != previous and available[2] and s_flag:
        if maze[i][j-1] in "-FL":
            visited = path_finding((i,j-1), coordinates, maze, visited) 
            if s_check:
                s_flag = False
        elif  maze[i][j-1] == "S":
            return visited
    
    # Right
    if (i,j+1) != previous and available[3] and s_flag:
        if maze[i][j+1] in "-J7":
            visited = path_finding((i,j+1), coordinates, maze, visited)
            if s_check:
                s_flag = False
        elif  maze[i][j+1] == "S":
            return visited
                
    return visited


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

visited = []
visited = path_finding(start, start, maze, visited) 
visited.sort()
print(visited)

inner_cells = []
for i in range(len(maze)):
    # print(i)
    for j in range(len(maze[0])):
        count = 0
        consecutive_flag = True
        for jj in range(j,len(maze[0])):
            # print(i,jj, consecutive_flag,count)
            if (i,jj) in visited:
                if consecutive_flag: # and (i,jj):
                    count += 1
                    consecutive_flag = False
            else:
                consecutive_flag = True
        if count % 2 == 1 and (i,j) not in visited:
            inner_cells.append((i,j))
            print((i,j),count)
print(len(inner_cells))
# print(inner_cells)


"""Part 2 using one of my favorite facts from graphics engineering: lets say you have an enclosed shape, and you want to color every pixel inside of it. How do you know if a given pixel is inside the shape or not? Well, it turns out: if you shoot a ray in any direction from the pixel and it crosses the boundary an odd number of times, it's inside. if it crosses an even number of times, it's outside. Works for all enclosed shapes, even self-intersecting and non-convex ones.

It does, however, interact badly if your ray and one of the edges of the shape is collinear, so you have to be clever about it for this problem."""
