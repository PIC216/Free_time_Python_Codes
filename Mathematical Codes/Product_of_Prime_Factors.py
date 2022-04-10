"""
This code takes a number as input and returns the product of it's prime factors in index form.
"""

import numpy as np
from collections import Counter
import sys

number = int(input())

def prime_finder(n):
  # finds all primes up to and including n
  # (where n>=2)
  prime_list = [2]
  for i in range(3,n+1):
    prime_factors = [x for x in prime_list if i % x == 0]
    if len(prime_factors) == 0:
      prime_list.append(i)
  return prime_list 

primes = prime_finder(int(number/2 + 2))

#print(primes,"\n")

prime_factors = [x for x in primes if number%x == 0]

#print(prime_factors)
if len(prime_factors) == 0:
  print(number)
  exit()

actual_factors = []
while number != 1:
  p = prime_factors[0]
  if number%p == 0:
    actual_factors.append(p)
    number = number / p
  else:
    prime_factors.pop(0)
  #print(number)

# print(actual_factors)

factor_dict = Counter(actual_factors)
factor_set = list(set(actual_factors))
factor_set.sort()
factor_string = ""
for value in factor_set:
  factor_string += str(value)
  if factor_dict[value] in [2, 3]:
    factor_string += eval(r'"\u00b' + str(factor_dict[value]) + '"')
  elif factor_dict[value] > 3:
    factor_string += "^" + str(factor_dict[value])
  if value != factor_set[-1]:
    factor_string += " x "


print(factor_string)
