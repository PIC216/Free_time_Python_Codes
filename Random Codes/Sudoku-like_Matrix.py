"""
This code takes an input n and returns a matrix of size n where each row and column contain only 1 of each number from 1 to n.
"""

# import required packages
import numpy as np
import random

# Get user input for matrix size
n = int(input("n:"))

# Create an n x n matrix filled with numbers from 1 to n
matrix = np.full([n, n], range(1, n + 1))
  
# Function to shift elements in a specified row to the left
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

# Shift elements in each row of the matrix
for i in range(n):
 shift(matrix, i)

# Save the matrix after basic shifting
basic_matrix_shift = matrix

# Function to generate a random list of specified length
def random_list(length):
  list = []
  for i in range(length):
    list.append(i)
  random.shuffle(list)
  return list

# Generate two random lists for row and column rearrangement
ran1 = np.array(random_list(n))
ran2 = np.array(random_list(n))

# Rearrange rows based on the first random list
half_matrix_shift = basic_matrix_shift[ran1,]

# Rearrange colums based on the second random list
full_matrix_shift = half_matrix_shift[:,ran2]

# print final matrix
print(full_matrix_shift)
