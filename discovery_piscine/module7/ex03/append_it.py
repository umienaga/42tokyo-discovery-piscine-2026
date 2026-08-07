#!/usr/bin/env python3

import sys

sys_input = sys.argv[1:]

if len(sys_input) >= 1:

    for word in sys_input:
        
        if word.find("ism",len(word)-3) == -1:
            print(word+"ism")


else:
    print("none")


