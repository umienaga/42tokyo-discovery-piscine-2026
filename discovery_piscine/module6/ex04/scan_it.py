#!/usr/bin/env python3

import sys
import re

input_word = sys.argv[1:]

if len(input_word) == 2:
    word_count = re.findall(input_word[0],input_word[1])
   
    if len(word_count) >= 1:
        print(len(word_count))

    else:
        print("none")

else:

    print("none")



