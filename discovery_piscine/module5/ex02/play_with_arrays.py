#!/usr/bin/env python3

number = [2,8,9,48,8,22,-12,2]
new_number = []


print(str(number))

count = 0

while count+1  <= len(number):
        
    if number[count]+2 > 5:
        new_number.append(number[count]+2)

        count = count + 1
    
    else:
        count = count + 1


print(str(new_number))



