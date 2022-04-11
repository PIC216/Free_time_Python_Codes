"""
Code which takes a list of numbers (separated by commas) and returns the type of sequence it is and the next term in the sequence. 
Currently only works for linear, quadratic, geometric, and fibonacci sequences.
"""


import numpy as np
seq = input("Input a sequence: \n")
print(seq)

#practice sequence: seq = "6, 12, 24, 48"

# setting all types of sequence as initially false to be checked later in code
fibonacci = False
linear = False
quadratic = False
geometric = False

# turning sequence into list
seq = np.array(seq.split(","))
seq = [int(i) for i in seq]

if len(seq) < 4:
  raise TypeError("Sequences must have at least 4 numbers.")

#function to find the difference between 2 numbers in a sequence, used 3 times in code
def diff(list):
  diff = []
  for i in range(len(list)-1):
    diff.append(list[i+1] - list[i])
  return diff


#firstly checking for geometric sequence
geo_check = []
for i in range(len(seq)-1):
  geo_check.append(seq[i+1]/seq[i])
if len(set(geo_check))==1:
  geometric = True
  b = int(geo_check[0])
  a1 = seq[0]/b
  if a1==int(a1):
    a = int(a1)
  else:
    a = a1
  d = seq[-1]*b

#finding the first difference for sequence, used in all other types of sequence
first_diff = diff(seq)

# checking for Fibonacci sequence next
fib_check = []
for i in range(len(first_diff)-1):
  fib_check.append(seq[i]-first_diff[i+1])
if fib_check[0]==0 and len(set(fib_check))==1 and not geometric:
  fibonacci = True
  d = seq[-1]+seq[-2]

# now checking for linear sequence
if len(set(first_diff))==1 and not fibonacci and not geometric:
  linear = True
  b = first_diff[0]
  a = seq[0] - b
  d = seq[-1] + b

# finally checking for quadratic
if not linear and not fibonacci and not geometric:
  second_diff = diff(first_diff)
  if len(set(second_diff))==1:
    quadratic = True
    c = int(second_diff[0]/2)
    quad = []
    for i in range(1,len(seq)+1):
      quad.append(c*i**2)
    seq2 = np.subtract(seq,quad)
    dif2 = diff(seq2)
    b = dif2[0]
    a = seq2[0] - b
    n = len(seq)+1
    d = c*n**2 + b*n + a

#now long if/print statement to print what's needed for each sequence type.
if linear:
  print(f"This is a linear sequence.\nThe Nth term is: {b}n + {a} \nThe next number in the sequence is {d}.")
elif quadratic:
  print(f"This is a quadratic sequence.\nThe Nth term is: {c}n\u00b2 + {b}n + {a}\nThe next number in the sequence is {d}.")
elif fibonacci:
  print(f"This is a Fibonacci sequence. \nThe next number in the sequence is {d}.")
elif geometric:
  print(f"This is a geometric sequence.\nThe Nth term is {a}*{b}^n \nThe next term in the sequence is {d}.")
else:
  print("I don't know this sequence (yet)")
