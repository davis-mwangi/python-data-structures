# python conditions
# a == b Equals
# a != b Not Equals
# a < b  Less than
# a <= b Less than or equal to
# a > b Greater than
# a >= b Greater than or equal to

a = 33
b =  33

if a >  b:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")   
else:
    print("a is greater than b")

# short hand if
if a > b: print("a is greater than b")   

# Ternary operators / Conditional Expressions
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c=  500

if a > b and c > a:
    print("Both conditions are True")

if  a > b or a > c:
    print("At least one of the conditions is True")

# Nested if
x =  41
if x > 10:
    print("Above 10,")
    if x > 20 :
        print("and also above 20!")   
    else:
        print("but not above 20")  

# pass for empty if
a =  33
b = 200
if b > a:
    pass          
