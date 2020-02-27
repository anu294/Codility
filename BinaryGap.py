# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#the largest integer to deal with
MAXINT = 2147483647

def solution(N):
    """
    Determines the maximum binary gap in an integer
    :param N: a positive integer (between 1 and 2million odd)
    :return a: a count of the longest sequence of zeros in the binary representation of the integer
    
    """
    # protect code against crazy input
    if not isinstance(N,int):
        raise TypeError("Input must be an integer")
    if N<1:
        raise ValueError("Input must be a positive integer")
    if N>MAXINT:
        raise ValueError("Input must be a positive integer less than 2147483647")

    #convert number to string containg '0' and '1' binary chars
    a = str(bin(N))[2:]
    #count the bits in the sequence
    count=0
    #the longest binary gap: Use NONE to denote no gap yet found
    maxCount=0
    for elem in a:
      if elem =='0':
        count+=1
      elif elem =='1':
        maxCount = count if maxCount < count else maxCount 
        count=0
    return maxCount
    #pass a

print (solution(-1))
