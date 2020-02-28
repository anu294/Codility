#for decimal related calculations
import math
def solution(X, Y, D):
    """
    determines minimum number of jumps from a position X to a position equal to or greater than Y
    :X param: Beginning position for jumps
    :Y param: End position for jumps
    :D param: Fixed distance for jumps
    :J return: Jump count to be returned
    """
    
    #Calculate closest jump less than or equal to desired distance
    J = math.floor((Y-X)/D)
    #Decide if J needs to take one more step to complete
    J = (J+1) if (Y-X)%D > 0 else J
    
    return J;

print (solution(10,30,30))
#https://app.codility.com/demo/results/trainingCQW674-8RU/
