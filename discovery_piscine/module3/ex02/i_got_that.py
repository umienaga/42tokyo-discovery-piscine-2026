#!/usr/bin/env python3

user_says = str(input("What you gotta say? : ").strip())

while True:
    if user_says == str("STOP"):
        break
    user_says = str(input("I got that! Anything else? : ").strip())
    
