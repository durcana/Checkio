#Input: Words as a set of strings.
#Output: True if one item in string is the suffix of another item in string.

def checkio(words_set):
    for word1 in words_set:
        for word2 in words_set:
            if word1 != word2:
                if word1 == word2[len(word2)-len(word1):]:
                    return True
                    
    return False
