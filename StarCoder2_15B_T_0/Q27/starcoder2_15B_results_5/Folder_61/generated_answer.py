def insert_after_index(lst):
    """
    Insert an element after a specific index in a list.

    Args:
        lst (list): The list to modify.

    Returns:
        list: A new list with the element inserted at the correct index.
    """
    return lst[:5] + [7] + lst[5:]