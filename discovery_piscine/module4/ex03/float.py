#!/usr/bin/env python3

number = input("Give me a number: ").strip()

flo_num = float(number)

if "." in number:

    parts = number.split(".")

    if len(parts) > 1 and parts[1].isdigit() and int(parts[1]) == 0:
        print("This number is an integer.")

    else:
        print("This number is a decimal.")

else:
    print("This number is an integer.")

