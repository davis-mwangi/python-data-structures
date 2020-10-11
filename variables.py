myvar = "David"
_my_val = "Mwangi"
myvar2="Irungu"

print(myvar)
print(_my_val)
print(myvar2)

x ,y ,z = "Orange","Banana","Apples"
print(x)
print(y)
print(z)
print(x + y +z)

num1= 10
num2 =5
print(num1 + num2)

# Global Functions
x = "Awesome"
def myFunc():
    x = "Fantastic"
    # Create global variable inside a function
    global y
    y = "Fantastic"
    print("Python is "+ y)

myFunc()
print(y)