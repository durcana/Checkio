#Input: An arbitrary number of arguments as numbers (int, float).
#Output: The difference between maximum and minimum as a number (int, float) as long as there's 2 or more arguments.
#If number of arguments is less than 2, return 0


def checkio(*args):
    number_list = []
    for number in args:
        number_list.append(number)
    number_list.sort()
    if len(number_list) > 1:
        return number_list[len(number_list) - 1] - number_list[0]
    else:
        return 0
