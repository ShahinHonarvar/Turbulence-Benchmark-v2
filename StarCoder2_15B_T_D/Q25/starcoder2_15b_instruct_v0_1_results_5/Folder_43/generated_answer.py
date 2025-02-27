def insert_at_index(lst):
    """
    Insert [28, 53] at index 29 in the given list and return the new list.
    """
    new_list = lst[:]
    new_list.insert(29, [28, 53])
    return new_list