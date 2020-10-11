# True or False
a = 200
b = 33

if  b > a:
    print("b is greater that a")
else:
    print("b is not greater than a")
    
# Evaluate values
# Any String is True, except empty 
print(bool("Hello")) # Returns True
print(bool(" "))     # Returns True
print(bool(""))      # Returns False

# Any number is True, except is 0
print(bool(123)) # Returns True
print(bool(0))   # Returns False

# Any list, tuple,set and dictionary is True except empty ones
x = bool(["apple","cherry","orange"])
print(x)

# Values that evaluate to False "", [], (),{}, 0, None, False
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))  

# Functions can return a boolean
def myFunction():
    return False

if myFunction():
    print("YES!")
else:
    print("NO!")     

# Check is instance
x = 200
print(isinstance(x, int))    