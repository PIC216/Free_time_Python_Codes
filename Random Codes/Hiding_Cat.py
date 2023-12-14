"""
I recently found a video on youtube that discussed the perfect solution for solving a Microsoft interview riddle, the hiding cat puzzle.
The problem is that there is a cat hiding in a box numbered 1 to 5, each turn you get to guess where the cat is but if you guess wrong then the cat will move one box left or right. What is the best strategy for ensuring you always find the cat?
The solution was interesting but I also started to consider how it might be possible to simulate the hiding cat in code and use the code to practice finding the cat. Here is said code (though I have edited it to allow for a different number of boxes):
"""

# import package
import random

# ask user how many boxes should be included
length = int(input("How many boxes?"))
# create list of empty boxes
boxes = ["-" for i in range(length - 1)]
# insert box with cat in in random position
boxes.insert(random.randint(0, length), "cat")


# create function to move cat 1 box to the left
def moveLeft(arr):
    catx = arr.index("cat")
    arr.pop(catx)
    arr.insert(catx - 1, "cat")
    return arr

# create function to move cat 1 box to the right
def moveRight(arr):
    catx = arr.index("cat")
    arr.pop(catx)
    arr.insert(catx + 1, "cat")
    return arr


# create function to move cat
def moveCat(boxes):
    cat = boxes.index("cat")
    if cat == 0:
        # cat must move right if already at the far left
        boxes = moveRight(boxes)
    elif cat == length - 1:
        # car must move left if already at the far right
        boxes = moveLeft(boxes)
    else:
        # if cat can move either left or right it moves in a random direction
        rand = random.randint(0, 1)
        if rand == 0:
            boxes = moveRight(boxes)
        elif rand == 1:
            boxes = moveLeft(boxes)
    return boxes

# cat starts as not being found 
cat_found = False

while not cat_found:
    value = int(input("Guess:"))
    # determines current box that cat is in
    cat = boxes.index("cat") + 1
    if not value in range(length+1):
        # allows repeat guess (without cat moving) if guess is out of the range of the number of boxes
        print(f"Please guess a box between 1 and {length}.")
    elif value == cat:
        # ends game once cat is found
        print("You've found the cat!")
        cat_found = True
    else:
        # cat moves if guess is wrong
        boxes = moveCat(boxes)
        print("Sorry, try again")
