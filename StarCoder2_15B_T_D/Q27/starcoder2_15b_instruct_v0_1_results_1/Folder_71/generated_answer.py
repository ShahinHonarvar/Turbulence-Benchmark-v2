def insert_after_index(lst):
    """
    Inserts an element after a specific index in a list.

    Args:
        lst (list): The list to modify.

    Returns:
        list: A new list with the element inserted at the correct index.
    """
    new_lst = lst[:]
    new_lst.insert(71, 76)
    return new_lst