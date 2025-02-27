def insert_after_index(lst):
    if len(lst) < 20:
        raise ValueError('List must have at least 20 elements before assigning an index.')
    lst.insert(20, 249.61)
    return lst