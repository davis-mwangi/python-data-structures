def longest_common_subsequence(x,y):

    # Find the length of the strings
    m = len(x)
    n = len(y)

    #  initialize the array to store our values
    table = [[None for i in range(n + 1)] for i in range(m+1)]
    # print(table)

    for i in range(m+1):
        for j in range (n+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif x[i -1] == y[j -1]:
                table[i][j] =  1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i][j -1], table[i-1][j])   
    index =  table[m][n]   
    print(index)    

    # Create a character arrat to store the lcs string
    lcs = ["" for x in range(index +1)]  
    print(lcs)
    lcs[index] = ""  
    print(lcs)
    # Start from the right-most-bottom-most corner and one by one 
    # store characters in lcs[]  
    i = m
    j = n

    while i > 0 and j > 0:
        # if the current character in x[]an y[]are same, then 
        # current character is part of lcs

        if x[i - 1] == y[j - 1]:
            lcs[index - 1] = x[i -1]
            i -=1
            j -=1
            index -=1

        # if not same, then find the larger of two and go in the direction of 
        # larger value
        elif table[i-1][j] > table[i][j-1]:
            i -=1
        else:
            j -=1
    return "".join(lcs)          

x = "AGGTAB"
y = "GXTXAYB"
z = longest_common_subsequence(x,y)
print(z)
# Time complexity O(mn)