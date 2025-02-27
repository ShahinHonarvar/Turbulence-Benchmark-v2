def insert_at_index(lst):
    """
    Insert 15 at index 99 in the given list and return the new list.
    """
    return lst[:99] + [15] + lst[99:]