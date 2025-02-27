def insert_after_index(lst):
    """
    Insert an element after a specific index in a list.
    """
    index = 51
    element = 304.62
    new_list = lst.copy()
    new_list.insert(index + 1, element)
    return new_list