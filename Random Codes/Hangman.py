"""
Here is my code for a game of hangman, with animals as the words, where you are allowed a maximum of 10 wrong guesses.
"""

import random


def convert_string(string):
    list = []
    list[:0] = string
    return list


def convert_list(list):
    str = ""
    for item in list:
      str = str + item + " "
    return str


word_list = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle' \
            ' ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda' \
            ' parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork' \
            ' swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
word = word_list[random.randint(0,len(word_list)-1)]

str = convert_string(word)

#print(str1)
guesses = []
guesses_left = 10
result = ["_"]

while guesses_left > 0 and "_" in result:
  guess = input("Your guess:").lower()
  guesses.append(guess)
  # print(f"Your guess: {guesses[-1]}\n")
  check = guess in str
  if check:
    print("Your guess was right!")
  else:
    guesses_left -= 1
    if guesses_left == 0:
      print("Uh oh, that was your last guess! \nSorry, you lose.")
    else:
      print(f"Uh oh, you now only have {guesses_left} guesses left...")
  result = [x if x in guesses else "_" for x in str]
  f_result = convert_list(result)
  print(f"{f_result} \n\n")
  if "_" not in result:
    print("Congratulations, you've found the word!!!")
