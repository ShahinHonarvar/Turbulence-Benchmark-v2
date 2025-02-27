def insert_at_index(lst):
    """
    Insert a number at a specific index in a list.

    Args:
        lst (list): The input list.

    Returns:
        list: A new list with the number 7 inserted at index 4.
    """
    return lst[:4] + [7] + lst[4:]