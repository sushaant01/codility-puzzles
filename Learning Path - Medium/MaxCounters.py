def MaxCounters(N,A):
    arrayMaxCounter = [0] * N
    MaxCounter = 0
    lastMaxCounter = 0
    for i in A:
        if i > N :
           lastMaxCounter = MaxCounter
        else:
            if arrayMaxCounter[i-1] <  lastMaxCounter:
                arrayMaxCounter[i-1] = lastMaxCounter + 1
            else :
                arrayMaxCounter[i-1] += 1
            if arrayMaxCounter[i-1] > MaxCounter:
                MaxCounter = arrayMaxCounter[i-1]
    if A[len(A)-1] > N :
        for i in range(len(arrayMaxCounter)):
           arrayMaxCounter[i] = MaxCounter    
    else: 
        for i in range(len(arrayMaxCounter)):
            if arrayMaxCounter[i] < lastMaxCounter :
                arrayMaxCounter[i] = lastMaxCounter
    return arrayMaxCounter
    pass


        
print(MaxCounters(5,[3,4,4,6,1,4,4]))        
