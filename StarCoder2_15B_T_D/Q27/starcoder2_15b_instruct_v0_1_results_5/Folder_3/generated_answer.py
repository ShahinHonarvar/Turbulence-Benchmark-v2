def insert_after_index(lst):
    idx = lst.index(31) + 1
    lst.insert(idx, 88)
    lst.insert(idx + 1, 51)
    return lst