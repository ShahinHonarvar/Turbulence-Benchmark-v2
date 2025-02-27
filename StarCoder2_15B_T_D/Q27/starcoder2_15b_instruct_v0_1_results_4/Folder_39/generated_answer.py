def insert_after_index(lst):
    """
    Insert [47, 22] after index 97 in the given list and return the resulting list.
    """
    return lst[:98] + [47, 22] + lst[98:]