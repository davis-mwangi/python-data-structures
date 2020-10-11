x = "Hello"
y = 'Hello'

print(x)
print(y)

## Multiline Strings ##
a = """ This is a
multiline string, I'm excited
to learn python """
print(a)

## Strings as Arrays ##
a ="Hello, World"
print(a[1])
 
# Slicing ##
b = "Hello, World"
print(b[2:5]) #from position 2 to position 5(no included)

# Negative indexing
b = "Hello, World"
print(b[-5: -2]) # from position 5 to position 2(not included)

#String length
a = "Hello, World"
print(len(a))

# strip() - removes white spaces from beginning or the end
a =  "   Hello, World   "
print(a.strip())  # returns "Hello, World"

# lower()
print(a.lower())

# upper()
print(a.upper())

#  replace()
print(a.replace("H", "J"))

# split()
print(a.split(",")) # returns ["Hello","World"]

##  Check String ##

txt = "The rain in Kenya stays mainly in the plain"
x =  "ain" in txt
print(x)
y =  "ain" not in txt
print(y)

# String concatenation
a = "Hello"
b = "World"

c = a  + " "+  b
print(c)

## String format ##
age = 36
height =5.6
txt = "My name is John, and I am {0}  and height {1}"
print(txt.format(age,height))

## Escape Character ##
txt =  "We are the so-called \"Vikings\" from the North"
print(txt)

# \' single quote
# \" double quote
# \\ backslash
# \n new  line
# \t Tab
# \b backspace

"""
Method	Description
capitalize()    => Converts the first character to upper case
casefold()      => Converts string into lower case
center()        => Returns a centered string
count()	        => Returns the number of times a specified value occurs in a string
encode()	    => Returns an encoded version of the string
endswith()	    => Returns true if the string ends with the specified value
expandtabs()	=> Sets the tab size of the string
find()	        => Searches the string for a specified value and returns the position of where it was found
format()	    => Formats specified values in a string
format_map()	=> Formats specified values in a string
index()	        => Searches the string for a specified value and returns the position of where it was found
isalnum()	    => Returns True if all characters in the string are alphanumeric
isalpha()	    => Returns True if all characters in the string are in the alphabet
isdecimal()   	=> Returns True if all characters in the string are decimals
isdigit()	    => Returns True if all characters in the string are digits
isidentifier()	=> Returns True if the string is an identifier
islower()	    => Returns True if all characters in the string are lower case
isnumeric()	    => Returns True if all characters in the string are numeric
isprintable()	=> Returns True if all characters in the string are printable
isspace()	    => Returns True if all characters in the string are whitespaces
istitle()	    => Returns True if the string follows the rules of a title
isupper()	    => Returns True if all characters in the string are upper case
join()	        => Joins the elements of an iterable to the end of the string
ljust()	        => Returns a left justified version of the string
lower()	        => Converts a string into lower case
lstrip()	    => Returns a left trim version of the string
maketrans()	    => Returns a translation table to be used in translations
partition()	    => Returns a tuple where the string is parted into three parts
replace()	    => Returns a string where a specified value is replaced with a specified value
rfind()	        => Searches the string for a specified value and returns the last position of where it was found
rindex()	    => Searches the string for a specified value and returns the last position of where it was found
rjust()	        => Returns a right justified version of the string
rpartition()	=> Returns a tuple where the string is parted into three parts
rsplit()	    => Splits the string at the specified separator, and returns a list
rstrip()	    => Returns a right trim version of the string
split()	        => Splits the string at the specified separator, and returns a list
splitlines()	=> Splits the string at line breaks and returns a list
startswith()	=> Returns true if the string starts with the specified value
strip()	        => Returns a trimmed version of the string
swapcase()	    => Swaps cases, lower case becomes upper case and vice versa
title()	        => Converts the first character of each word to upper case
translate()	    => Returns a translated string
upper()  	    => Converts a string into upper case
zfill()	        => Fills the string with a specified number of 0 values at the beginning
"""

## Check contains digits only##
ONLY_DIGITS = "45566336754493420932877387482372374982374823749823283974232237238472392309230923849023848234580383485342234287943943094234745374657346578465783467843653748654376837463847654382382938793287492326"

NOT_ONLY_DIGITS = "45566336754493420932877387482372374982374823749823283974232237238472392309230923849023848234580383485342234287943943094234745374657346578465783467843653748654376837463847654382382938793287492326P"
print(ONLY_DIGITS.isdigit())
print(NOT_ONLY_DIGITS.isdigit())