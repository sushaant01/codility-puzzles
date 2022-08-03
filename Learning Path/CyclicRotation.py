def CyclicRotation(A, K):
    # write your code in Python 3.6
    if  len(A) > 0 :
        counter = (K % len(A) ) 
        B = [0]*len(A)
        if counter >= 0 :
            for var in A :
                if counter >= len(A) :
                    counter = counter - len(A) 
                B[counter] = var
                counter = counter + 1
        return B
    else:
        return A
pass

# testing 
print (CyclicRotation([3, 8, 9, 7, 6], 1))
print (CyclicRotation([3, 8, 9, 7, 6], 2))
print (CyclicRotation([3, 8, 9, 7, 6], 3))
print (CyclicRotation([3, 8, 9, 7, 6], 4))
print (CyclicRotation([3, 8, 9, 7, 6], 5))
