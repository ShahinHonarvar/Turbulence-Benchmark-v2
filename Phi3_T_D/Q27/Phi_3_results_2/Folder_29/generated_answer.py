def insert_after_index(lst):
    if 96 in lst:
        idx = lst.index(96) + 1
        lst.insert(idx, 36)
    return lst