#Input: A password as a string.
#Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean.
# In the results you will see the converted results.

def checkio(data):

    if len(data) < 10:
        return False
    elif data == data.lower():
            return False
    elif data == data.upper():
        return False
    return any(char.isdigit() for char in data)
