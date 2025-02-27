def insert_at_index(lst):
    if len(lst) >= 56:
        lst.insert(56, 54)
    else:
        lst += [None] * (56 - len(lst)) + [54]
    return lst