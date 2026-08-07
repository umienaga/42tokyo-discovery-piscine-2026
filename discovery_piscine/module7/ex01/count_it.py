#!/usr/bin/env python3

import sys

sys_input = sys.argv[1:]

if len(sys_input) >= 1:
    print("parameters: "+str(len(sys_input)))
    for word in sys_input:
        print(word+": "+str(len(word)))
    
    
else:
    print("none")

