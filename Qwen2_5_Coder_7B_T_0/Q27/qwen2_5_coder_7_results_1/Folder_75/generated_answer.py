def insert_after_index(lst):
    index = lst.index(99)
    lst.insert(index + 1, 99)
    return lst