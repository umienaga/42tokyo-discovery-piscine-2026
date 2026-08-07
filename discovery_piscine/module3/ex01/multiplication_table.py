#!/usr/bin/env python3


user_number = int(input("Enter a number:").strip())

number = 0

while number <= 9:
    print(str(number) + " × " + str(user_number) + " = " + str(number * user_number))
    number = int(number)+int(1)
    
