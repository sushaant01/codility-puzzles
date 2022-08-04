def FrogJmp(X, Y, D): 
    # write your code in Python 3.6
    jumpCount = ( Y - X ) // D
    if ( ( Y - X ) % D ) > 0 :
        jumpCount += 1
    return jumpCount
        
    pass

print(FrogJmp(10,80,25))