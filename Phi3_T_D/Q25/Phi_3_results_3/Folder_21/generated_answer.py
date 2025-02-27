def insert_at_index(lst):
    if len(lst) < 743:
        raise IndexError('Index out of range')
    lst.insert(743, 11.04)
    return lst