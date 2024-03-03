#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            print('{}'.format(chr(ord(i) - 32)), end='')
        else:
            print('{}{}'.format(i, '' if i !=i[-1] else i, '\n'))
