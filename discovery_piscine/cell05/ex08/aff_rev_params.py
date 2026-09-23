#!/usr/bin/env python3
import sys
if len(sys.argv) < 3:
    print("none")
else:
    params = sys.argv[1:]
    for param in reversed(params):
        print(param)