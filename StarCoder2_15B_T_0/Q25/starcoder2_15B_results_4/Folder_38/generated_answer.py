def insert_at_index(lst):
    """
    Insert an element at a specific index in a list.

    Args:
        lst (list): The list to modify.

    Returns:
        list: A new list with the element inserted at the specified index.
    """
    return lst[:89] + [86] + lst[89:]