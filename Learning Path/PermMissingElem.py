
def PermMissingElem(A): 
    # write your code in Python 3.6
    size = len(A) + 1
    if size > 1 :
        total = size * (size + 1) // 2
        sum = 0
        for i in range(size-1):
            sum = sum + A [i]
        return ( total - sum)
    else: 
        return 0
    pass

print (PermMissingElem([1,2,3,4,6]))
print (PermMissingElem([2]))
print (PermMissingElem([]))