# A RegEx (Regular Expression)  is a sequence of characters that forms a search pattern

import re
txt =  "The rain in Kenya"
x = re.search("^The.*Kenya$",txt)

if x:
    print("Yes we have a match")
else:
    print("No match")    