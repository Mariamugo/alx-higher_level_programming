#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = sys.argv[1:]
    total = 0
    for i in result:
        total += int(i) 
    print("{}".format(total))
