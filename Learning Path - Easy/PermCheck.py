# this solution is working on my local machine , but getting memory error when submitting using codility giving me 83%
def PermCheck(A):
    # write your code in Python 3.6
    arrayCount = 0 
    maxNumber = 0
    for i in A :
        if i > maxNumber:
            maxNumber = i
    if maxNumber < len(A):       
        maxNumber = len(A)
    counter = [0]*maxNumber
    count = 0
    while arrayCount < len(A):
        if A[arrayCount] != counter[A[arrayCount]-1]:
            counter[A[arrayCount]-1] = A[arrayCount]
            count += 1
        arrayCount += 1
    if count == maxNumber:
        return 1 
    else:
        return 0
    pass

print (PermCheck([1000000000]));
#print (PermCheck([4,1,3,2]));
#print (PermCheck([4,1,3]));
#print (PermCheck([2]));
#print (PermCheck([1]));
#print (PermCheck([1,4,1]));
#print (PermCheck([1,2,3,4,5,7]));
