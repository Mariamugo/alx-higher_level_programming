#!/usr/bin/python3
for i in range(0, 99):
    print('{:02d},'.format(i), end=' ')
    if i == 98:
        i += 1
        print('{}'.format(i), end='\n')
