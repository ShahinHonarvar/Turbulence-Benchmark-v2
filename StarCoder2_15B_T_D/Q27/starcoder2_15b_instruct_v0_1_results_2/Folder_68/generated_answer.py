def insert_after_index(lst):
    index = lst.index(7) + 1
    lst.insert(index, [1, 7])
    return lst