def insert_after_index(lst):
    """
    Insert an element after a specified index in a list.

    Args:
        lst (list): The list to modify.

    Returns:
        list: A new list with the element inserted at the correct index.
    """
    new_lst = lst[:]
    new_lst.insert(1 + 1, 141.02)
    return new_lst