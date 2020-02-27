# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#restriction on length of array and shifts
MAXSHIFT = 100
def solution(A, K):
    """
    determines the resultant array after circular shifting it by K times
    :A param: array with N elements
    :K param: number of shifts

    """
    # protect code against crazy input
    if not isinstance(K,int):
        raise TypeError("Number of shifts must be an integer")
    if K<0 or K>MAXSHIFT or len(A)<0 or len(A)>MAXSHIFT:
        raise ValueError("Input must be a in the range [0,100]")

    #length of array
    arrLength = len(A)

    #returning blank array if N is 0
    if arrLength==0:
        return [];
        
    #new array
    updatedArr=[]
    k1 = K % arrLength
    for elem in range(0, arrLength):
      updatedArr+= [A[((elem-k1)%arrLength)]]
    
    return updatedArr

    #pass
print (solution([3, 8, 9, 7, 6], ))
