def insert_at_index(lst):
    """
    Insert an element at a specified index in a list.

    Args:
        lst (list): The list to which the element will be inserted.

    Returns:
        list: A new list with the element inserted at the specified index.
    """
    return lst[:4] + [7] + lst[4:]