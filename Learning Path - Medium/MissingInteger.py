def MissingInteger(A):
    minElement =  1
    countArray = [0] * 100001
    for i in A :
        if i > 0 and i < 100001 :
            if countArray[i-1] == 0 :
                countArray[i-1] = 1
    for i in range(len(countArray)):
        if countArray[i] == 0 :
            minElement = i + 1
            break
    return minElement
    pass

#print(MissingInteger([-1000000, 1000000]))
#print(MissingInteger([1, 3, 6, 4, 1, 2]))
#print(MissingInteger([-2,-3,-4,1]))
#print(MissingInteger([-1]))
#print(MissingInteger([1]))

print(MissingInteger([1,2,3,4,5,6,7,8,9,10]))