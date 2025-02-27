def insert_at_index(lst):
    """
    Insert 11.04 at index 743 in the given list and return the new list.
    """
    return lst[:743] + [11.04] + lst[743:]