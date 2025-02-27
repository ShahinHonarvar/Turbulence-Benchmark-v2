def insert_after_index(lst):
    if len(lst) <= 412:
        raise IndexError('Index out of range')
    lst.insert(413, 668)
    return lst