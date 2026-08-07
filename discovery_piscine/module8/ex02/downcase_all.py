#!/usr/bin/env python3

import sys

sys_input = sys.argv[1:]


def downcase_it(word):

    return word.lower()

if len(sys_input) >= 1:
    for low in sys_input:
        print(downcase_it(low))


else:
    print("none")


