def FrogRiverOne(X,A):
    count = [0] * X
    counter = 0
    returnVal = 0
    arrayCount = 0
    found = False
    while arrayCount < len(A) :
        if A[arrayCount] != count[A[arrayCount]-1] :
            count[A[arrayCount]-1] = A[arrayCount]
            counter += 1
        if counter == X:
            found = True
            break
        arrayCount += 1        
    if found :
        returnVal = arrayCount
    else:
        returnVal = - 1      
    return returnVal
    pass

print(FrogRiverOne(5,[1,3,1,4,2,3,5,4]))
print("------------------")
print(FrogRiverOne(3,[1,2,3]))
print("------------------")
print(FrogRiverOne(1,[1]))
print("------------------")
print(FrogRiverOne(2,[1,1,1]))
print("------------------")
print(FrogRiverOne(2,[2,2,2,2,2]))
print("------------------")
print(FrogRiverOne(2,[2,2,2,2,2]))
print("------------------")
print(FrogRiverOne(3, [1, 3, 1, 3, 2, 1, 3]))