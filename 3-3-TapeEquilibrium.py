#the largest integer to deal with
MAXLENGTH = 100000

def solution(A):
    """
    Determines the minimum difference between sum of two sub arrays
    :param A: an array with N positive integers 
    :return minDif: minimum difference between sums of sub arrays
    
    """
    N = len(A)
    # protect code against crazy input
    if N>MAXLENGTH:
        raise ValueError("Input must an array smaller than 10~6")
    
    print(A)
    
    #Find sum of all elements in the array
    total,prevElem=[],0
    for elem in A:
      total += [(prevElem + elem)]
      prevElem = prevElem + elem
    sumTotal = total[N-1]
    minDif=None
    print(total)
    for elem in range(N-1):
      dif=abs((sumTotal-total[elem])-total[elem])
      if minDif is None:
          minDif=dif
      print("dif "+str(dif))
      minDif=dif if (minDif>dif) else minDif
    #if minDif is None:
          #minDif=sumTotal
    return minDif
    

print (solution([59, -999, 20]))
#https://app.codility.com/demo/results/training557SAA-A64/
