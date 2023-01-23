#!/usr/bin/env python 3

import re

date_pattern = re.compile("#[A-Fa-f0-9]{6}")

#The dates should match the pattern dd-MMM-yyyy, where dd is a two-digit day, MMM is a three-letter month abbreviation, and yyyy is a four-digit year.

date = input("The date the event will take place on: ")
match = date_pattern.match(date)

if match:
print("Date found:", match.group())
else:
print("No date found.")

