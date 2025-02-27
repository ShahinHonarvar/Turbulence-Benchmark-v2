def insert_after_index(lst):
    """
    Insert the values [86, 77] into the list `lst` at the index immediately succeeding index 48.
    """
    new_lst = lst[:]
    new_lst.insert(49, 86)
    new_lst.insert(50, 77)
    return new_lst