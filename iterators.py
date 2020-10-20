# An interator is an object that contains countable number of values

# Lists, tuples, dictionaries and sets are all iterable objects
mytuple = ("apple","banana","cherry")
myit =  iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# strings are iterable objects
mystr = "banana"
myit =  iter(mystr)
print(next(myit))

# Create an iterator
# To create an object/class as iterator you have to implement the methods  __iter__() and __next__() to your object
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
           x = self.a
           self.a +=1
           return x
        else:
            raise StopIteration   

myclass =  MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))

for x in myiter:
    print(x)
