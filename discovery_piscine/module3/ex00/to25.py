#!/usr/bin/env python3

number = int(input("Enter a number less than 25:").strip())

if number > 25:
    print("Error")

else:
    while number <= 25:
        print("Inside the loop, my variable is " + str(number))
        number = int(number) + int(1)
