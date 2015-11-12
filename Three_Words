#Input: A string with words.
#Output: The answer as a boolean. If three words in a row, return True.

def checkio(words):
    words = words.split()
    if len(words) < 3:
        return False
    else:
        alpha = []
        for w in words:
            if w.isalpha():
                alpha.append(w)
                if len(alpha) == 3:
                    return True
            else:
                alpha = []
        return False
