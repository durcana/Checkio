#A text as a string.
#Whether the sentence is a pangram or not as a boolean.

def check_pangram(text):
    alphabet = list(map(chr, range(97, 123)))
    text = text.lower()
    for letter in alphabet:
        if letter not in text:
            return False
    return True
