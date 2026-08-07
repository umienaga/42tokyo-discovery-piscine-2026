#!/usr/bin/env python3

import sys

sys_input = sys.argv[1:]

if len(sys_input) == 2:
    
    if int(sys_input[0]) < int(sys_input[1]):
        
        print(list(range(int(sys_input[0]),int(sys_input[1])+1)))

    else:
        print("none")
else:
    print("none")

