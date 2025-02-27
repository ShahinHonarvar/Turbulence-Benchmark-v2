def insert_after_index(lst):
    if len(lst) < 57:
        raise IndexError('Index 56 is out of range')
    lst.insert(57, 54)
    return lst