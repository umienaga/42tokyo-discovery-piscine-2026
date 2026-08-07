#!/usr/bin/env python3

import sys

sys_input = sys.argv[1:]

if len(sys_input) ==  1:
    user_input = input("What was the parameter? ").strip()
    
    if sys_input[0] == user_input:
        print("Good job!")

    else:
        print("Nope, sorry...")

else:
    print("none")



