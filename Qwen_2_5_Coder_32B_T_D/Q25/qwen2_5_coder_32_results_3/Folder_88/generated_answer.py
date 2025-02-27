def insert_at_index(lst):
    if len(lst) < 91:
        lst += [None] * (91 - len(lst))
    lst.insert(91, [46, 13])
    return lst