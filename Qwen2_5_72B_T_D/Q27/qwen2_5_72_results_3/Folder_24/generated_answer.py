def insert_after_index(lst):
    index = lst.index(42) + 1
    lst.insert(index, 53)
    return lst