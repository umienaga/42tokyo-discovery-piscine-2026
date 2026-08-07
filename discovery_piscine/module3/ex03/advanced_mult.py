#!/usr/bin/env python3

first_number = 0
result = ""


while first_number <= 10:
    second_number = 0
    result = ""
    
    while second_number <= 10:
        result = str(result) + " " + str(first_number * second_number)
        
        second_number = second_number + 1

    print("Table of " + str(first_number) + ":" + str(result))
    first_number = first_number + 1
        
        

