def insert_after_index(lst):
    """
    Insert an element after a specific index in a list.

    Args:
        lst (list): The input list.

    Returns:
        list: A new list with the element inserted at the correct index.
    """
    return lst[:36] + [88] + lst[36:]