#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 96 < ord(i) < 123:
            print('{}'.format(chr(ord(i) - 32)), end='')
    print(i)
