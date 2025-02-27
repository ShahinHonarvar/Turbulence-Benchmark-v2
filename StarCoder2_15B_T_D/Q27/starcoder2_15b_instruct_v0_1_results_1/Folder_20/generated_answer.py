def insert_after_index(lst):
    """
    Insert [54, 96] after index 32 in the given list and return the modified list.
    """
    return lst[:33] + [54, 96] + lst[33:]