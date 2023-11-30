'''
If you can't use the ** operator or
the power function, how can you find
the power of a number?

This code takes two inputs, number and
power and returns a sentence with the
answer.

Note: this code does have it's
limitations, it is souly focusing
on the regular cases of calculating
a positive integer to the power of
a positive integer.
'''

print("""Please give a number and a
         power. To end the calculations
         press 0 for either number
         or power.""")

while True:
  number = int(input("Number: ")
  if number == 0:
    break
  power = int(input("Power: "))
  if power == 0:
    break
  counter = power
  value = number
  while counter > 1:
    value *= number
    counter -= 1
  print(f"""{number} to the power of
            {power} is {value}.""")
