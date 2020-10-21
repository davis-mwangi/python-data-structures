"""
Given a value N, if we want to make change for N cents, and we have infinite supply of
 each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? 
 The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: 
{1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and 
S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, 
{2,3,5} and {5,5}. So the output should be 5.
"""
# Dynamic programming 
def count(S , N):
    m = len(S)
    my_table = [[0 for x in range(m)] for x in range(N + 1)]
    print(my_table)

    # Fill the entries for 0 values case (n = 0)
    for i  in range(m):
        my_table[0][i] = 1
    print(my_table)    

    # Fill rest of the table entries in botton up manner
    for i in range(1, N+1):
        for j in range(m):

            # Count of solutions including S[j]
            x = my_table[i - S[j]][j] if i - S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y =  my_table[i][j-1] if j >= 1  else 0

            # total amount
            my_table[i][j] = x + y
    return my_table[N][m-1]

# Time complexity O(mn)    
x = count([1,2,3],4)  
print(x)

# Optimized solution with O(n) space complexity
def count2(S,N):
    m = len(S)
    # table[i] will be storing the number of solutions for value i.
    # We need n+ 1 rows as the table is constructed in bottom up manner  using the
    # base case n = 0

    # Initialize all table values as 0
    table = [0 for k in range(N+1)]
    print(table)

    # Base case (If given value is 0)
    table[0] = 1

    print (table)

    # Pick all coins one by one and update table[] values 
    # after the index greater than or equal to the value of the 
    # picked coin
    for i in range(0, m):
        for  j in range(S[i], N+1 ):
            table[j] += table[j - S[i]]
    print(table)        
    return table[N]        

x = count2([1,2,3],4)    
print(x)
