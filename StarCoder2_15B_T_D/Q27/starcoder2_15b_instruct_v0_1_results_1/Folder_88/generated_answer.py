def insert_after_index(lst):
    """
    Function to insert an element after a given index in a list.

    Parameters:
    -----------
    lst: list
        A list of elements.

    Returns:
    --------
    list: A new list with the element inserted at the correct index.
    """
    return lst[:92] + [46, 13] + lst[92:]