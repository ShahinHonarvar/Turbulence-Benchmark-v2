def insert_after_index(lst):
    """
    Insert an element after a specific index in a list.

    Args:
        lst (list): The input list.

    Returns:
        list: A new list with the element inserted at the correct index.
    """
    new_lst = lst[:]
    new_lst.insert(lst.index(89) + 1, 86)
    return new_lst