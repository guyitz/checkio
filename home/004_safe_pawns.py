def _test():
    from doctest import testmod
    testmod(verbose=True)


def get_down_left(pos):
    if pos[0] == 'a' or pos[1] == '1':
        return None
    else:
        return chr(ord(pos[0]) - 1) + str(int(pos[1]) - 1)


def get_down_right(pos):
    if pos[0] == 'h' or pos[1] == '1':
        return None
    else:
        return chr(ord(pos[0]) + 1) + str(int(pos[1]) - 1)


def safe_pawns(pos_set):
    """
    >>> safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
    6
    >>> safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})
    1

    :param list_of_elements_to_check:
    :return:
    """
    counter = 0
    for pos in pos_set:
        if get_down_left(pos) in pos_set or get_down_right(pos) in pos_set:
            counter += 1
    return counter


# Other solutions I liked...

def safe_pawns(pawns):
    safePawns = 0

    for col, row in pawns:

        defenseRow = str(int(row) - 1)
        defenseLeft = chr(ord(col) - 1) + defenseRow
        defenseRight = chr(ord(col) + 1) + defenseRow

        if defenseLeft in pawns or defenseRight in pawns:
            safePawns += 1

    return safePawns

