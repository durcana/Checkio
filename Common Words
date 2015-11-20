#Input: Two arguments as strings, words separated by , instead of space
#Output: The common words as a string, separated by , instead of space

def checkio(first, second):
    same_words = []
    first = list(first.split(","))
    second = list(second.split(","))

    for word_first in first:
        for word_second in second:
            if word_first == word_second:
                same_words.append(word_first)
    same_words = sorted(same_words)            
    return ",".join(same_words)
