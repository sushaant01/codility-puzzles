
def TapeEquilibrium(A):
    # write your code in Python 3.6
    sum = 0
    for i in range(len(A)):
        sum = sum + A[i]
    minTotal = 1000000
    leftSide = 0
    for i in range(len(A)-1):
        leftSide = leftSide + A[i]
        rightSide = sum - leftSide
        newMinVal = abs(rightSide - leftSide)
        if newMinVal < minTotal :
            minTotal =  newMinVal
    return minTotal
    pass

print(TapeEquilibrium([-100,100]))
print(TapeEquilibrium([3,1,2,4,3]))

