#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    found = False
    for char in text:
        if char == "z":
            print("z", end="")
            found = True
    if not found:
        print("none")
    else:
        print()