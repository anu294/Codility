#the largest integer to deal with
MAXLENGTH = 100000

def solution(X, A):
    """
    Determines the minimum time in which leaves are present at every position between 1 an d X
    :param A: an array with N positive integers less than X
    :param X: an integer representing total number of positions until goal
    :return time: minimum time array length when all positive int until x have occurred
    
    """
    N = len(A)
    # protect code against crazy input
    if N>MAXLENGTH or X>MAXLENGTH:
        raise ValueError("Input must an array length and positions smaller than 10~6")
    
     
    #Instantiate a counter array to remember occurance
    count = [0] * (X + 1)
    done=0
    for elem in A:
      if count[elem] is 0:
          #Update occurance and total number of positions covered
          count[elem]=1
          done+=1
          if done==X:
              return A.index(elem)

    return -1    

print (solution(5,[1,3,1,4,2,3,5,4]))
#https://app.codility.com/demo/results/trainingBWV5RU-FXH/
