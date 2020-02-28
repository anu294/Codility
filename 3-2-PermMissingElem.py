#the largest integer to deal with
MAXLENGTH = 100000

def solution(A):
    """
    Determines the missing number in a range of positiver integers
    :param A: an array with N positive integers within the range [1,N+1]
    :return e: missing element to be returned
    
    """
    N = len(A)
    # protect code against crazy input
    if N>MAXLENGTH:
        raise ValueError("Input must an array smaller than 10~6")
    
    
    #sum of all positive integers upto N+1
    accruedSum = int((N+1)*(N+2)/2)
    #Find sum of all elements in the array
    total=0
    for elem in A:
      total += elem
    e = accruedSum - total
    return e
    

print (solution([2,3,1,5]))
#https://app.codility.com/demo/results/training557SAA-A64/
