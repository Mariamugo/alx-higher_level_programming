#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
print(f'Last digit of', end=' ')
if abs(last_digit) > 5:
    print(f'{number} is {last_digit} and is greater than 5')
elif (abs(last_digit) < 6) && (abs(last_digit) != 0):
    print(f'{number} is {last_digit} and is less than 6 and not 0')
else:
    print(f'{number} is {last_digit} and is 0')
