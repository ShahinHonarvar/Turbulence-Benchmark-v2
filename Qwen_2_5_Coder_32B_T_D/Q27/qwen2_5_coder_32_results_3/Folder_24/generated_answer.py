def insert_after_index(lst):
    if 42 in lst:
        idx = lst.index(42) + 1
        lst.insert(idx, 53)
    return lst