try:
    print("Hello")
except NameError:
    print("Variable x is not defined")    
except:
    print("An exception occurred")    
else:
    print("Nothing went Wrong")    

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")        

# Raise an exception
x  = -1

if x < 0 :
    raise Exception("Sorry , no numbers below zero")