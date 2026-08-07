#!/usr/bin/env python3

import sys



sys_input = sys.argv[1:]

if len(sys_input) == 1:
   
    output = ""

    for z in sys_input[0]:
        if z == "z":
            output += "z" 
        
    if output:

        print(output)
   
    else:
        print("none")

else:
    print("none")

