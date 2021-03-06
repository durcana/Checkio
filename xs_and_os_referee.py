#Input: A game result as a list of strings (unicode).
#Output: "X", "O" or "D" as a string.

def checkio(field):
    for row in field:
        if row[0] == row[1] == row[2] and row[0] !='.':
            if row[0] == 'O':
                return 'O'
            elif row[0] == 'X':
                return 'X'
    rotated_field = zip(*field)
    for row in rotated_field:
        if row[0] == row[1] == row[2] and row[0] !='.':
            if row[0] == 'O':
                return 'O'
            elif row[0] == 'X':
                return 'X'

    if field[0][0] == field [1][1] == field [2][2] and field[1][1] != '.':
        return field[1][1]
    elif field [2][0] == field[1][1] == field[0][2] and field[1][1] != '.':
        return field[1][1]
    for x in range(3):
        for y in range(3):
            if field[x][y] == '.':
                pass
        return "D"


    return "D" or "X" or "O"

#From Checkio:
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"
