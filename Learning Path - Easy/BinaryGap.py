def BinaryGap(N):
    # write your code in Python 3.6
    binVal = bin(N)    
    stringVal = binVal[2:]
    returnVal = 0
    counterVal = 0
    for var in stringVal :
        if var == "0" :
            counterVal = counterVal + 1
        else :
            if returnVal < counterVal :
                returnVal = counterVal 
            counterVal = 0
    return returnVal
pass

# testing   
print(BinaryGap(15))
print(BinaryGap(152))
