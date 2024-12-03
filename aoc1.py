from collections import Counter

"""
Advent of Code Day 1:

Part1:
Find the sum of distances in two lists of integer numbers by comparing first minimum of each
list (left and right), then second min of each list and so on.

Part2:
Calculate total similarity score by adding up each number in the left list after multiplying 
by the number of times it appears in the right list.
"""
#Build lists
file_path = 'C:/Users/aserb/Downloads/message.txt'
try:
    with open(file_path, 'r') as file:
        left_list = []
        right_list = []
        for line in file:
            line.strip()
            num1, num2 = line.split()
            left_list.append(int(num1))
            right_list.append(int(num2))
except FileNotFoundError:
    print("The file was not found!")

except IOError:
    print("The file could not be read!")

ll_copy = left_list.copy()
rl_copy = right_list.copy()

#part 1
net_distance = 0
for i in range(len(left_list)):
    lm = min(left_list)
    rm = min(right_list)
    left_list.pop(left_list.index(min(left_list)))
    right_list.pop(right_list.index(min(right_list)))
    net_distance += abs(rm - lm)

print(net_distance)

#part 2
rl_dict = {}
for number in rl_copy:
    if number in rl_dict:
        rl_dict[number] += 1
    else:
        rl_dict[number] = 1

ll_set = set(ll_copy)
running_total = 0
for number in ll_set:
    if number in rl_dict:
        running_total += rl_dict[number] * number

print(running_total)