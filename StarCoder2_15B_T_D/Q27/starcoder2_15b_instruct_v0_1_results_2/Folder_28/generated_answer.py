def insert_after_index(lst):
    """
    Inserts 49 into the list at index 75, returning a new list with the element inserted.
    """
    return lst[:75] + [49] + lst[75:]