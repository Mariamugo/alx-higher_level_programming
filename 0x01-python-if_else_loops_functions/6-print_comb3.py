#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        print('{}'.format(i), end='')
        if i == 8:
            print('{}'.format(j), end='\n')
        else:
            print('{},'.format(j), end=' ')
