#!/usr/bin/env python3

import sys

count = 0

parameters = sys.argv[1:]
parameters.reverse()

if len(parameters) >= 2:
    
    while count <= len(parameters)-1:

        print(parameters[count])
        count = count + 1

        

else:
    print("none")
