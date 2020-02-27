# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#restriction on length of array and shifts
MAXSHIFT = 100
def solution(A):
    """
    determines the non duplicate item
    :A param: array with N elements
    :K param: number of shifts

    """
    
    #length of array
    N = len(A)

    # protect code against crazy input
    if N % 2 ==0:
        raise ValueError("Odd number of values is to be input")
    
    #remove duplicates
    updatedDict={}
    for elem in range(0, N):
        if updatedDict.get(A[elem])==1:
            del updatedDict[A[elem]]
        else:
            updatedDict[A[elem]]= 1;
    
    return list(updatedDict.keys())[0];

    #pass
print (solution([3, 8, 8, 7, 3]))
