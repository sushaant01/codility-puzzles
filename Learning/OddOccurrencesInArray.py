def OddOccurrencesInArray(A):
    # write your code in Python 3.6
    A.sort()
    returnVal = 0
    counter = 0
    while counter < len(A) - 1:
        if A[counter] == A[counter+1]: 
            counter = counter + 2
        else:
            returnVal = A[counter]
            counter = counter + 1
    if A[len(A) - 2] != A[len(A) - 1] :
        returnVal = A[len(A) - 1] 

    return returnVal
    
    pass


print(OddOccurrencesInArray([0,2,40,10,23,10,40,2,0]))
print(OddOccurrencesInArray([0,3,6,9,9,9,9,3,6,0,0,0,11]))