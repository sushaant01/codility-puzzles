
## this is still in development and working 46% when I submitted 
def TapeEquilibrium(A):
    # write your code in Python 3.6
    sum = 0
    for i in range(len(A)):
        sum = sum + A[i]
    minTotal = sum
    leftSide = 0
    for i in range(len(A)):
        leftSide = leftSide + A[i]
        rightSide = sum - leftSide
        newMinVal = abs(rightSide - leftSide)
        if newMinVal < minTotal :
            minTotal =  newMinVal
    return minTotal
    pass

#print(TapeEquilibrium([-2,-1,1,2]))
print(TapeEquilibrium([3,1,2,4,3]))

