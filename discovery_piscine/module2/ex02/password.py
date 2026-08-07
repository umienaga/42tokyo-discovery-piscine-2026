#!/usr/bin/env python

password = "Python is awesome"

user_pass = str(input().strip())

if user_pass == password:
    print("ACCESS GRANTED")
    
else:
    print("ACCESS DENIED")


