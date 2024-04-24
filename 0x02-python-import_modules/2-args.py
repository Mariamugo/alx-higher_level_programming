#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = len(sys.argv) - 1
    if result == 1:
        print("{} argument:".format(result))
    elif result == 0:
        print("{} arguments.".format(result))
    else:
        print("{} arguments:".format(result))
    for i in range(1, result + 1):
        print("{}: {}".format(i, sys.argv[i]))
