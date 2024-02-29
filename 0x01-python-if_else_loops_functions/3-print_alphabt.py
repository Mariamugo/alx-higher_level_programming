#!/usr/bin/python3
for value in range(97, 123):
    if chr(value) not in [e, q]:
        print('{}'.format(chr(value)), end='')
