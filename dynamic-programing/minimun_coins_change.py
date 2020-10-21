import sys
"""
Given a value V, if we want to make change for V cents, and we have infinite supply 
of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins
 to make the change?
"""
def minCoins(coins, n):
    m =  len(coins) 

    # table[i] willbe storing the minimun number of coins required for i
    # value. So table[n] will have result
    table = [0 for i in range(n+1)]

    # Base case (If given n is 0)
    table[0] = 0

    # Initiliaze all table values as Infinite
    for i in range(1,n+1):
        table[i] = sys.maxsize
    print(table)
    # Compute minimun coins required for all values from 1 to n
    for i in range(1, n + 1):
        # Go through all coins smaller than i
        for j in range(m):
            if coins[j]  <= i:
                result = table[i - coins[j]]
                if result != sys.maxsize and  1 + result < table[i] :
                    table[i] = result + 1
        print(table)            
    return table[n]                 
        

x = minCoins([9,6,5,1], 11)    
print(x)