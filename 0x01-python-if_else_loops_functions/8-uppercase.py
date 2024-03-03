#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            print('{}'.format(chr(ord(i) - 32)), end='')
        else:
            print(i, '{}'.format('' if i != str[-1] else '\n'))
