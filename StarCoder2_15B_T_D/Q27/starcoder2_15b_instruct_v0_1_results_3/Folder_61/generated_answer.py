def insert_after_index(lst):
    """
    Insert an element at a specific index in a list and return the new list.

    Args:
        lst (list): The list to insert into.

    Returns:
        list: A new list with the element inserted at the specified index.
    """
    new_lst = lst[:]
    new_lst.insert(4 + 1, 7)
    return new_lst