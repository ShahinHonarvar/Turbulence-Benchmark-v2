def insert_after_index(lst):
    if not isinstance(lst, list):
        raise ValueError('The argument must be a list')
    lst.insert(2, 478.12)
    return lst