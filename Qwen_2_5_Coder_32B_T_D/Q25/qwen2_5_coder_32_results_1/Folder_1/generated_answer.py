def insert_at_index(lst):
    if len(lst) < 93:
        lst.extend([None] * (93 - len(lst)))
    lst.insert(93, [33, 78])
    return lst