def insert_after_index(lst):
    if 70 in lst:
        index = lst.index(70)
        lst.insert(index + 1, 76)
    return lst