#Input: Two arguments. A text as a string (unicode for py2) and words as a set of strings (unicode for py2).
#Output: The number of words in the text as an integer.


def count_words(text, words):
    text = text.lower()
    count = []
    for w in words:
        for i in range(len(text)):
            if w[0] == text[i]:
                if w[0:len(w)] == text[i:i+len(w)]:
                    if w not in count:
                        count.append(w)
                
    return len(count)
