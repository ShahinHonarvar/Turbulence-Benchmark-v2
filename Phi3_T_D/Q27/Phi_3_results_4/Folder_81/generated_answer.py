def insert_after_index(lst):
    if len(lst) <= 28:
        raise ValueError('List must contain at least 29 elements')
    lst.insert(29, 20)
    return lst