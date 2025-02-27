def insert_after_index(lst):
    """
    Insert an element after the index of another element in a list.

    Args:
        lst (list): The input list.

    Returns:
        list: A new list with the element inserted.
    """
    new_lst = lst[:]
    new_lst.insert(lst.index(90) + 1, 80)
    return new_lst