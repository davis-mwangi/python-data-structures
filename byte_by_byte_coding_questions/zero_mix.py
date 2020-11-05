"""
Given a boolean matrix, update it so that if any cell is true, all the cells in that
row and column are true.
"""
def zeroMatrix(matrix):
    #Verify if the input array is nonzero
    if(len(matrix) == 0 or len(matrix[0]) == 0):
        return

    #Determin whether the first row or first column is true
    rowZero = False
    colZero = False

    for i in matrix[0]:
        rowZero |= i   

    for i in matrix:
        colZero |= i[0]    

    # For each cell not in the first row/column, if it is true, set the
    # cell in the first row/same column and column/same row to be true
    for i in range(1, len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j]:
                matrix[i][0] =  True
                matrix[0][j] =  True

    # Go through the first column and set each row to True where cell in the 
    # the first column is True
    for i in range(1, len(matrix)):
        if matrix[i][0]:
            for j in range(1, len(matrix[i])):
                  matrix[i][j] = True

    # Repeat for the rows
    for j in range(1, len(matrix[0])):
        if matrix[0][j]:
            for i in range(1, len(matrix)):
                matrix[i][j] = True  

    # Set first row/column to True if necessary
    if(rowZero):
        for j in range(len(matrix[0])):
            matrix[0][j]= True

    if colZero:
        for i in range(len(matrix)):
            matrix[i][0] = True

    return matrix


list_ = [ [True, False , False ], [False, False , False ],[False, False , False ]]
x = zeroMatrix(list_)
print(x)