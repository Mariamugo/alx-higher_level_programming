#!/usr/bin/python3
for value in range(97, 123):
    if chr(value) not in 'eq':
        print('{}'.format(chr(value)), end='')
