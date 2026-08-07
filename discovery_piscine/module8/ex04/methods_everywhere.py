#!/usr/bin/env python3

import sys

sys_input = sys.argv[1:]

def shrink(eight_up):
    eight_up = eight_up[:8]

    return eight_up

def enlarge(eight_low):
    
    while len(eight_low) < 8:
        eight_low += "Z"
    
    return eight_low

if len(sys_input) >= 1:

    for word in sys_input:

        if len(word) < 8:
            print(enlarge(word))

        elif len(word) > 8:
            print(shrink(word))

        else:
            print(word)

else:
    print("none")
