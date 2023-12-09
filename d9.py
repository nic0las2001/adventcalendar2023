import math, numpy as np

input = open("d9.txt","r")

sums = []; sums2 = []
for line in input:
    nums = np.array(list(map(int, line.split())))
    steps = [nums]
    while np.linalg.norm(nums) != 0: # magnitude of array
        nums = nums[1:] - nums[0:-1]
        steps.append((nums))
    for i in range(-1,-len(steps),-1):
        # Interpolate end val
        new_step = np.append(steps[i-1], steps[i-1][-1]+steps[i][-1])
        # Interpolate beg val
        new_step = np.insert(new_step, 0, steps[i-1][0]-steps[i][0])
        steps[i-1] = new_step
    sums.append(steps[0][-1])
    sums2.append(steps[0][0])

print("P1: ", sum(sums))
print("P2: ", sum(sums2))