def insert_after_index(lst):
    """
    Inserts 37 into the list at index 44, returning a new list.
    """
    return lst[:44] + [37] + lst[44:]