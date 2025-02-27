def insert_after_index(lst):
    index = lst.index(87)
    lst.insert(index + 1, 78)
    lst.insert(index + 2, 16)
    return lst