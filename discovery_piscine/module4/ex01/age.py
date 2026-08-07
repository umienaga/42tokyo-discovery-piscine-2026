#!/usr/bin/env python3

you_age = int(input("Please tell me your age: ").strip())

multiple = 1

print("Your are curretly " + str(you_age) + " years old.")

while multiple <= 3:
    print("In" +str(multiple * 10) +"years, you'll be "+ str(you_age + multiple * 10) + " years old.")
    multiple = multiple + 1
