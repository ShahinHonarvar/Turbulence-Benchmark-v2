def insert_after_index(lst):
    """
    Insert 0.78 after index 49 in the given list and return the new list.
    """
    new_lst = lst[:]
    new_lst.insert(50, 0.78)
    return new_lst