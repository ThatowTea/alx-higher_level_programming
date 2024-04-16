#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    nlist = len(sys.argv) - 1
    if nlist == 0:
        print("0 arguments.")
    elif nlist == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nlist))
    for i in range(nlist):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
