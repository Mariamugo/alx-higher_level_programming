#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
print(f'Last digit of', end=' ')
if last_digit > 5:
    print(f'{number} is {last_digit} and is greater than 5')
elif last_digit < 6 and last_digit != 0:
    if number < 0:
        last_digit = -abs(last_digit)
    print(f'{number} is {last_digit} and is less than 6 and not 0')
else:
    print(f'{number} is {last_digit} and is 0')
