#!/usr/bin/env python3

first_number = int(input("Enter the first number").strip())

second_number = int(input("Enter the second number").strip())

print(str(first_number) + "×" + str(second_number) + "=" + str(first_number * second_number))

if first_number * second_number < 0:
    print("The result is negative.")

elif first_number * second_number > 0:
    print("The result is positive.")

else:
    print("The result is positive and negative.") 
