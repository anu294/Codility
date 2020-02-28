#the largest integer to deal with
MAXLENGTH = 100000

def solution(N, A):
    """
    Determines the minimum time in which leaves are present at every position between 1 an d X
    :param A: an array with N positive integers less than X
    :param X: an integer representing total number of positions until goal
    :return time: minimum time array length when all positive int until x have occurred
    
    """
    L = len(A)
    # protect code against crazy input
    if L<=0 or L>MAXLENGTH or L>MAXLENGTH:
        raise ValueError("Input must an array length and positions smaller than 10~6")
    
     
    #Instantiate a counter array to remember occurance
    count = [0] * (N)

    countMax=0
    for elem in A:
        if elem > N:
            count = [countMax] * (N)
        else:
            count[elem-1] +=1

            countMax = count[elem-1] if countMax < count[elem-1] else countMax

    return count;    

print (solution(99999,[99999,99999,99999,99999,99999,99999,99999,100000,3,6,3]))
#https://app.codility.com/demo/results/trainingBWV5RU-FXH/
