def insert_at_index(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list.')
    lst.insert(761, 925)
    return lst