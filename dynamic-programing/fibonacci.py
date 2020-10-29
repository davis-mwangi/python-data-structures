
# Top down approach (Recursion)
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        sum = fib(n -1 )+  fib(n -2)
        return sum
    
x = fib(9)       
print(x)              

# (Dynamic programming)
fibarray = [0,1]
def fibonacci(n):
    if n <= 0:
        return 0
    elif n <= len(fibarray):
        return fibarray[n -1]    
    else:
        temp_fib = fibonacci(n -1) + fibonacci(n -2)
        fibarray.append(temp_fib)
        print(fibarray)
        return temp_fib    

y = fibonacci(9)
print(y)    

# Space optimized

def fib3(n):
    a =0
    b = 1
    if n  <= 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c =  a + b
            a = b
            b = c       
        return b     

x =  fib3(9)
print(x)        