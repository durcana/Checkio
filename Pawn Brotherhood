#Input: Placed pawns coordinates as a set of strings, as a1, b5, etc.
#Output: The number of safe pawns as a integer.

def indexing(pawns):

    pawns_indexes = set()
    safe_indexes = set()

    for pawn in pawns:
        row = int(pawn[1]) - 1
        col = ord(pawn[0]) - 97
        pawns_indexes.add((row, col))
        safe_indexes.add((row + 1, col + 1))
        safe_indexes.add((row + 1, col - 1))

    safe_pawns(pawns_indexes, safe_indexes)

def safe_pawns(x, y):
    safe = 0
    for a in x:
        if a in y:
           safe += 1
    print safe
