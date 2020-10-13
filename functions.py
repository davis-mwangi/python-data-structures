def my_function1(fname):
    print("I'm refreshing python "+ fname
    )

my_function1("David")  # calling a function
my_function1("Charles")

# Arbitrary arguments , *args
def my_function2(*kids):
    print("The youngest child is "+kids[2])

my_function2("Faith","Tobias","Esther")    


# keyword arguments nornally shortened to kwargs in python
def my_function3(child3, child2, child1):
    print("The youngest is "+child3)
my_function3(child1="Ayub",child2="Emilly",child3="Kariuki")    


# Arbitrary keyword arguments, **kwargs
def my_function4(**kid):
    print("Hist last name is "+ kid["lname"])

my_function4(fname=" Tobia", lname="Elijah")    


# default parameter

def my_function5(country = "Kenya"):
    print("I am from "+ country)

my_function5("USA")
my_function5("UK") 
my_function5()  

# Passing a list as an argument

def my_function6(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]
my_function6(fruits)        


# Return values

def my_function7(x):
    return 5 * x

print(my_function7(3))    

# pass statement

def my_function8():
    pass
my_function8()

# Recursion
print("###### recursion ###########")
def tri_recursion(k):
    if (k > 0):
        result =  k + tri_recursion(k -1)
        print(result)
    else:
        result = 0    
    return result

tri_recursion(6)        