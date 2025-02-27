def insert_at_index(lst):
    if len(lst) < 76:
        lst += [None] * (76 - len(lst))
    lst.insert(76, [15, 51])
    return lst