#Input: A list of integers.
#Output: The list of the repeating integers.

def checkio(data):
    repeats = []
    for item in data:
        if data.count(item) == 1:
            pass
        elif data.count(item) >= 2:
            repeats.append(item)
    return repeats
