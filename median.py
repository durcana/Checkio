#Input: An array as a list of integers.
#Output: The median as a float or an integer.

def checkio(data):

    data.sort()
    if len(data) % 2 != 0:
        return data[(len(data)/2)]
    elif len(data) % 2 == 0:
        return (data[len(data)/2] + data[len(data)/2 - 1]) / 2.0
    return data[0]
