#Input: Placed pawns coordinates as a set of strings, as a1, b5, etc.
#Output: The number of safe pawns as a integer.

def safe_pawns(pawns):
    safe = 0
    pawns_indexes = []
 
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.append([row, col])

    for pawn in pawns_indexes:
        if [pawn[0] - 1, pawn[1] + 1] in pawns_indexes or [pawn[0] - 1, pawn[1] - 1] in pawns_indexes:
            safe += 1
    return safe
