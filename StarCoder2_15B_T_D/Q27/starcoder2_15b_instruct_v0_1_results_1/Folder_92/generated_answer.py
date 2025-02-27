def insert_after_index(lst):
    """
    Insert an element after a given index in a list.

    Args:
        lst (list): The list to modify.

    Returns:
        list: A new list with the element inserted.
    """
    new_lst = lst[:]
    new_lst.insert(1 + 1, 478.12)
    return new_lst