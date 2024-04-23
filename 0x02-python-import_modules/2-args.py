#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = len(sys.argv) - 1
    if result == 1:
        print("{} argument:".format(result))
    elif result == 0:
        print("{} argument.".format(result))
    else:
        print("{} arguments:".format(result))
    for i in range(1, result):
        print("{}: {}".format(i, result(i)))
