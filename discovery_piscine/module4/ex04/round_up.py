#!/usr/bin/env python3

user_num = input("Give me a number").strip()

num = float(user_num)

if "." in user_num:
    parts = user_num.split(".")
    
    right_parts = int(parts[1])
    left_parts = int(parts[0])

    if right_parts > 0:
        result = left_parts + 1

    else:
        result = left_parts

else:
    result = user_num


print(result)


