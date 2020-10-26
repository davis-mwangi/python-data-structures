"""
Given weights and values of n items, put these items in a knapsack of capacity W 
to get the maximum total value in the knapsack. In other words, given two integer 
arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with
 n items respectively. Also given an integer W which represents knapsack capacity, 
 find out the maximum value subset of val[] such that sum of the weights of this subset
  is smaller than or equal to W. You cannot break an item, 
either pick the complete item or don’t pick it (0-1 property).
"""

def knapSack(W,wt,val):
    n = len(val)
    table= [[0 for i in range(W+1)] for i in range(n+1)]

    #Build table[][] in bottom up mannner
    for i in range(n+1):
        for w in range(W+1):
            if i ==0 or w == 0:
                table[i][w] = 0
            elif  wt[i -1] <= w:
                table[i][w] = max(val[i-1]+table[i-1][w -wt[i-1]],table[i-1][w])
            else:
                table[i][w] =table[i-1][w]    
    return table[n][W]           

val =[60,100,120]
wt = [10,20,30]
W = 50
x =  knapSack(W,wt,val)
print(x)

def knapSack2(items, maxWeight):
    n = len(items)
    m = maxWeight
    X = [[0 for i  in range(m+1)] for i in range(n+1)]

    for i in range(n+1):
        for w in range(m+1):
            if i == 0 or w == 0:
                X[i][w] = 0 
            elif items[i -1].get("w") <= w:
                X[i][w] = max(X[i-1][w], items[i-1].get("v") + X[i -1][w - items[i-1].get("w")])
            else:
                X[i][w] = X[i-1][w]    
    return X[n][m]            


items = [ { 'w': 1, 'v':6 },{ 'w': 2, 'v':10 },{ 'w': 3, 'v':12 }]
maxWeight =5
x = knapSack2(items, maxWeight)
print(x)

