class MyClass:
    x = 5

# object 
p1 = MyClass()
print(p1.x)    


class Person:
    def __init__(self,name,age):
        """
        This is executed when a class is initiated
        """
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is "+ self.name)    

p1 =  Person("John", 26)   
print(p1.name)
print(p1.age)
p1.myfunc()

"""
The `self` parameter is a reference to the current instance of the class, and is used to access variables 
that belong to that class. It does ntot have to be name self but has to the first parametr of any
function.
"""

# Modify Object properties
p1.age = 40
print(p1.age)

#Delete object properties
del p1.age
# print(p1.age)

# Pass statement
class Person2:
    pass

# Delete objects
# del p1
print(p1)


