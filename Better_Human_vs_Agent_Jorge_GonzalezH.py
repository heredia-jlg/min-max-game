# Jorge Gonzalez-Heredia
# Assignment 5


import time

import math

def remove_num(chosen, list):

    temp = []

    in_set = False

    while not in_set:
        if chosen not in list:
            print("Integer is not in the set. Try another number.")
            chosen = int(input())
        else:
            in_set = True

    for index in list:
        if chosen % index != 0:
            temp.append(index)

    return temp

def div_game_max_value(alive):
    if len(alive) == 1:
        return [-1, alive[0]]
    elif len(alive) == 0:
        return [1, []]
    elif len(alive) == 2:
        return [1, alive[0]]
    else:
        h = -math.inf

        for a in alive:
            temp_result = div_game_min_value(remove_num(a, alive))
            temp_h = temp_result[0]

            if temp_h > h:
                h = temp_h
                best_action = temp_result[1]
                return [h, best_action]


def div_game_min_value(alive):
    if len(alive) == 1:
        return [1, alive[0]]
    elif len(alive) == 0:
        return [-1,[]]
    elif len(alive) == 2:
        return [-1, alive[0]]
    else:
        h = math.inf

        for a in alive:
            temp_result = div_game_max_value(remove_num(a,alive))
            temp_h = temp_result[0]
            if temp_h < h:
                h = temp_h
                best_action = temp_result[1]
                return [h, best_action]


def div_game_max_value_action(alive):
    action = div_game_max_value(alive)

    return action[1]


print("Enter your name: ")
name = input()
print("Enter a positive integer n: ")
n = int(input())
turn = 0

while turn > 2 or turn < 1:
    print("Enter 1 if you want to go first, 2 for second: ")
    turn = int(input())


remaining = []

for i in range(1, n + 1):
    if (n % i) == 0:
        remaining.append(i)

counter = turn
while len(remaining) != 0:
    # even for first odd for second
    print("Here are the remaining numbers: " + str(remaining))

    if counter % 2 != 0:
        txt = name + ", pick a number from the list above: "
        print(txt)
        print()
        chosen = int(input())
        remaining = remove_num(chosen, remaining)

    else:

        # agent chooses best action
        start = time.time()
        best = div_game_max_value_action(remaining)
        end = time.time()
        print("Time it took: " + str(end - start) )

        chosen = best
        txt = "My pick is " + str(chosen)
        print(txt)
        print()
        remaining = remove_num(chosen,remaining)

    counter += 1


if counter % 2 == 0:
    print(name + ', you lose')
else:
    print("I lost!")

