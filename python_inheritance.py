# Parent class -  class being inherited from (Base class)
# Child class  -  class that inherits from another class, (Derived class)

class Person:
    def __init__(self, fname,lname,age):
       self.firstname =  fname
       self.lastname =  lname
       self.myage   =  age

    def printname(self):
        print(self.firstname,self.lastname)   

x  = Person("David","Mwangi",26)     
x.printname()

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:


class Student(Person):
    def __init__(self,fname,lname, age, year):
        super().__init__(fname,lname,age)
        self.graduationyear = year # add properties

    # Add methods
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)    

x = Student("Mike","George", 27,2020)
x.printname()
print(x.graduationyear)
x.welcome()