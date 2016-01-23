#Input: Three arguments. X and Y as 0 or 1. An operation name as a string.
#Output: The result as 1 or 0.
#Precondition: x in (0, 1)
#y in (0, 1)
#operation in ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == "conjunction":
        return x and y
    elif operation == "disjunction":
        return x or y
    elif operation == "implication":
        return (not x) or y
    elif operation == "exclusive":
        return (x or y) and (not(x and y))
    elif operation == "equivalence":
        return not((x or y) and (not(x and y)))
