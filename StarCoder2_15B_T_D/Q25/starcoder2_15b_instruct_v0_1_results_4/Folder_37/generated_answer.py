def insert_at_index(lst):
    """
    Insert an element at a specified index in a list.

    Args:
        lst: The list to modify.

    Returns:
        A new list with the element inserted at the specified index.
    """
    new_lst = lst[:]
    new_lst.insert(35, 88)
    return new_lst