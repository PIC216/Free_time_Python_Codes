'''
This code was created to solve a problem in alevel from a game app: 100 doors challenge

You start with 9 lightbulbs where some are on and some are off; when you press one lightbulb, multiple lightbulbs will be turned off or on.
This code goes through pressing lightbulbs in a random order and it determines whether after about 15 presses you have turned on all lightbulbs.
Code returns whether a solution has been found and the order you need to press the lightbulbs in.
'''



import random

# Starting order of lightbulbs, x = on, - = off
light_bulbs = ["x", "x", "-", "-", "-", "-", "x", "-", "x"]

# Shows which lightbulbs are switched when one is pressed
# eg if you press lightbulb_4 you will switch lightbulbs 1, 4, and 7
lightbulb_1 = [1, 6, 8]
lightbulb_2 = [2, 6, 7, 9]
lightbulb_3 = [3, 5, 9]
lightbulb_4 = [4, 1, 7]
lightbulb_5 = [5, 1, 2, 3]
lightbulb_6 = [6, 4, 9]
lightbulb_7 = [7, 1, 3]
lightbulb_8 = [8, 4, 5]
lightbulb_9 = [9, 2, 8]

lightbulb_list = [lightbulb_1, lightbulb_2, lightbulb_3, lightbulb_4, lightbulb_5, lightbulb_6, lightbulb_7, lightbulb_8, lightbulb_9]

# function to turn the lightbulbs on or off
def switch(list_, val):
    if list_[val-1] == 'x':
        list_[val-1] = '-'
    elif list_[val-1] == '-':
        list_[val-1] = 'x'
    return list_


# Function which checks whether only one more lightbulb press is needed to solve the game
def check(list_):
    for var in lightbulb_list:
        lights_off = []
        lights_on = []
        for val1 in range(1, 10):
            if val1 in var:
                lights_off.append(light_bulbs[val1-1])
            else:
                lights_on.append(light_bulbs[val1-1])
        if len(set(lights_off)) == 1 and len(set(lights_on)) == 1 and lights_off[0] == '-' and lights_on[0] == 'x':
            trials.append(var[0])
            return True
        else:
            continue
    return False


trials = []
i = 0
solved = False

# 15 is chosen to keep the number of potential trials short, can be changed if you are
# happy to follow a longer sequence of presses
while i < 15 and not solved:
    choice = random.choice(lightbulb_list)
    trials.append(choice[0])
    for val in choice:
        light_bulbs = switch(light_bulbs, val)
    print(choice[0])
    print(light_bulbs)
    if check(light_bulbs):
        solved = True
    i += 1


# if game has been solved consecutive duplicate lightbulb presses are removed
if solved:
    print("\nSolved!!!\n")
    new_trials = []
    for i in range(len(trials)):
        if not new_trials:
            new_trials.append(trials[i])
        elif trials[i] == new_trials[-1]:
            new_trials.pop()
        else:
            new_trials.append(trials[i])

    print(new_trials)
else:
    print("\nNot solved :(")
