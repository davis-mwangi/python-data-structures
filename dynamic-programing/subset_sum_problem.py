# Given a set of non-negative integegers e.g set[] = {3,34,4,12,5,2} and a value sum e.g sum =9
# , determine if there is a subset of the given set with sum equal to given sum

def isSubSet(myset, sum):
    n = len(myset)
    # The value of the subset[i][j] will be true if there is a subset[0..j] with sum equal to i
    subset = ([[False for i in range(sum + 1)] for i in range(n + 1)])

    #If sum is o, then answer is true
    for i in range(n + 1):
        subset[i][0] = True

        # If sum is not 0 set is empty
        # the answer is false
        for i in range(1, sum + 1):
            subset[0][i] = False

        # Fill the subset table in bottom up manner
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if j < myset[i - 1]:
                    subset[i][j] = subset[ i - 1][j]  
                if j  >= myset[i - 1]:
                    subset[i][j] =  (subset[i-1][j] or subset[i -1][j - myset[i -1]])
               
    return subset[n][sum]

x = isSubSet([3,34,4,12,5,2], 9)
print(x)    