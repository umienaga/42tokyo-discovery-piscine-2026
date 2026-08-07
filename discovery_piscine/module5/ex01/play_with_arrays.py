#!/usr/bin/env python3

number = [2,8,9,48,8,22,-12,2]
new_number = []


print("Original array: " + str(number))

count = 0

while count+1  <= len(number):
    new_number.append(number[count]+2)
    count = count + 1

print("New array: " +  str(new_number) )



