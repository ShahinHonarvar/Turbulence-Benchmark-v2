def insert_after_index(lst):
    """
    Insert an element at a specific index in a list.

    Args:
        lst (list): The list to modify.

    Returns:
        list: A new list with the element inserted at the specified index.
    """
    new_lst = lst[:]
    new_lst.insert(45, 76)
    return new_lst