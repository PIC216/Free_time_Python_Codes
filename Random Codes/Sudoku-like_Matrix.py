"""
This code takes an input n and returns a matrix of size n where each row and column contain only 1 of each number from 1 to n.
"""

import numpy as np
import random

n = int(input("n:"))
matrix = np.full([n,n], range(1,n+1))

#print(matrix,"\n")
  
def shift(mat, row):
  for i in range(row):
    a=[]
    for i in range(n):
      a.append(mat[row,0])
     # print(a)
      if i==n-1:
        mat[row,n-1] = a[0]
      else:
        mat[row,i] = mat[row,i+1]
  return mat

for i in range(n):
 shift(matrix, i)

basic_matrix_shift = matrix

#print(basic_matrix_shift, "\n")

def random_list(length):
  list = []
  for i in range(length):
    list.append(i)
  random.shuffle(list)
  return list

ran1 = np.array(random_list(n))
ran2 = np.array(random_list(n))

half_matrix_shift = basic_matrix_shift[ran1,]
#print(half_matrix_shift, "\n")
full_matrix_shift = half_matrix_shift[:,ran2]
print(full_matrix_shift)
