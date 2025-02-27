def insert_after_index(lst):
    index = lst.index(29) + 1
    lst.insert(index, 28)
    lst.insert(index + 1, 53)
    return lst