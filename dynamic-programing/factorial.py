
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n   

x = factorial(4)
print(x)

# Memoized solution
d = {}
def factorial2(n):
    if n in d:
        return[n]
    if n == 0:
        return 1
    else:
        y = factorial(n-1) * n
        d[n] = y
        print(d)
        return y   

x = factorial2(4)
print(x)