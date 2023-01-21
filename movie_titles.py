import re

pattern = re.compile(r"(.*) \((\d{4})\)")

#The movie titles should match the pattern "Title (yyyy)", where "Title" is any string of characters, and "yyyy" is a four-digit year.

def get_titles(title):
    match = pattern.match(title)

    if match:
        return("Title:", match.group(1)+" "+"Year:", match.group(2))
    else:
        return "Invalid title"
