#!/usr/bin/env python3

import sys
import re

input_word = sys.argv[1:]

if len(input_wd) == 2:
    word_count = re.findall(input_wd[0],input_wd[1])
   
    if len(word_count) >= 1:
        print(len(word_count))

    else:
        print("none")

else:

    print("none")



