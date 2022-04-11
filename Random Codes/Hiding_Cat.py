"""
I recently found a video on youtube that discussed the perfect solution for solving a Microsoft interview riddle, the hiding cat puzzle.
The problem is that there is a cat hiding in a box numbered 1 to 5, each turn you get to guess where the cat is but if you guess wrong then the cat will move one box left or right. What is the best strategy for ensuring you always find the cat?
The solution was interesting but I also started to consider how it might be possible to simulate the hiding cat in code and use the code to practice finding the cat. Here is said code (though I have edited it to allow for a different number of boxes):
"""

import random

length = int(input("How many boxes?"))
boxes = ["-" for i in range(length - 1)]
boxes.insert(random.randint(0, length), "cat")


# print(boxes)


def moveLeft(arr):
    catx = arr.index("cat")
    arr.pop(catx)
    arr.insert(catx - 1, "cat")
    return arr


def moveRight(arr):
    catx = arr.index("cat")
    arr.pop(catx)
    arr.insert(catx + 1, "cat")
    return arr


def moveCat(boxes):
    cat = boxes.index("cat")
    if cat == 0:
        boxes = moveRight(boxes)
    elif cat == length - 1:
        boxes = moveLeft(boxes)
    else:
        rand = random.randint(0, 1)
        if rand == 0:
            boxes = moveRight(boxes)
        elif rand == 1:
            boxes = moveLeft(boxes)
    return boxes


catFound = False

while not catFound:
    # print(boxes)
    value = int(input("Guess:"))
    cat = boxes.index("cat") + 1
    if value == cat:
        print("You've found the cat!")
        catFound = True
    else:
        boxes = moveCat(boxes)
        print("Sorry, try again")
