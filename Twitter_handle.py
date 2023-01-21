#!/usr/bin/python3
#Twitter handle that should match a certain pattern
#"@username" as a string of letters and digits.

import re

#The regular expression 
pattern = re.compile(r'@([a-zA-Z0-9]+)')
string = input("Enter your twitter handle: ")
match = re.search(pattern, string)

#If statement
if match:
    print(f"Your twitter handle is: @{string}")
else:
    print("No match found")
