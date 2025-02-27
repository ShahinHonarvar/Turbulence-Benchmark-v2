def insert_after_index(lst):
    index = lst.index(323) + 1
    lst.insert(index, 389)
    lst.insert(index + 1, 303)
    return lst