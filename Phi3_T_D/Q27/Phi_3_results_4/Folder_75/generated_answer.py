def insert_after_index(lst):
    if 99 in lst:
        index = lst.index(99) + 1
        lst.insert(index, 99)
    return lst