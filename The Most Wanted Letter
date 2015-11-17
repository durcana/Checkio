#Input: A text for analysis as a string.
#Output: The most frequent letter in lower case as a string.

def checkio(text):
    text = text.lower()
    dict = {}
    for letter in text:
        if letter in dict:
            dict[letter] += 1
        elif letter not in dict and letter.isalpha() == True:
            dict[letter] = 1
        else:
            pass


    return max(sorted(dict), key=dict.get)

    return 'a'
