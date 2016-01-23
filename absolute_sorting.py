#Input: An array of numbers , a tuple.
#Output: The list or tuple (but not a generator) sorted by absolute values in ascending order.

def checkio(numbers_array):
    abs_numbers = sorted([i if i > 0 else -i for i in numbers_array])
    answer = []
    
    for absnum in abs_numbers:
        if absnum not in numbers_array:
            answer.append(absnum * (-1))
        else:
            answer.append(absnum)
            
    return answer
