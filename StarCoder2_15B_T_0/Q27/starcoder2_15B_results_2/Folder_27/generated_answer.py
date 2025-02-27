def insert_after_index(lst):
    """
    Insert [41, 95] after index 85 in the given list and return the new list.
    """
    new_lst = lst[:]
    new_lst.insert(86, 41)
    new_lst.insert(87, 95)
    return new_lst