def insert_after_index(lst):
    if len(lst) < 100:
        raise IndexError('The list must contain at least 100 elements.')
    lst.insert(100, 15)
    return lst