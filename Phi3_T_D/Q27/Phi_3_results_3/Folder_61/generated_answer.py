def insert_after_index(lst):
    if len(lst) < 5:
        raise ValueError('List must have at least 5 elements for index 4 to exist.')
    lst.insert(5, 7)
    return lst