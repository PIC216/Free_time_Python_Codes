'''
Problem: If you can't use the ** operator or the power function, how can you find the power of a number?

This code takes two inputs, number and power, and returns a sentence with the answer.

Note: this code does have it's limitations, it is souly focusing on the regular cases of calculating
values to the power of a positive integer (or 0).
'''

print("""Please give a number and a power. To end the calculations press 0 for number.""")

while True:
    number = float(input("Number: "))
    if number == 0:
        break
    power = float(input("Power: "))
    if power == 0:
        value = 1
    elif power == int(power) and power > 0:
        power = int(power)
        value = 1
        for i in range(power):
            value = value*number
    else:
        print("Not an acceptable value for power")
        continue
             
    if number == int(number):
        number = int(number)
    if value == int(value):
        value = int(value)
             
    print(f"""{number} to the power of {power} is {value}.""")
