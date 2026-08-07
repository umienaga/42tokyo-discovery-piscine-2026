#!/usr/bin/env python3

def greetings(name = "noble stranger"):
    if isinstance(name, str) == True :
        return "Hello, " + str(name) + "."
        
        
    else:
        return "Error! It was not a name."


print(greetings("Alexandra"))
print(greetings("Wil"))
print(greetings())
print(greetings(31241))




