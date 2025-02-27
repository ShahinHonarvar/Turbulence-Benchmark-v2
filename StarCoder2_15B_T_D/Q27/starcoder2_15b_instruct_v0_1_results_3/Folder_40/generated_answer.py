def insert_after_index(lst):
    """
    Insert an element after a given index in a list.

    Args:
        lst (list): The input list.

    Returns:
        list: A new list with the element inserted at the correct index.
    """
    index = 4
    element = 856.69
    new_lst = lst[:]
    new_lst.insert(index + 1, element)
    return new_lst