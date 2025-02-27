def insert_after_index(lst):
    """
    Insert an element after a given index in a list.

    Args:
        lst (list): The list to insert the element into.

    Returns:
        list: A new list with the element inserted.
    """
    return lst[:3] + [8] + lst[3:]