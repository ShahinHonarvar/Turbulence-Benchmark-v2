def insert_after_index(lst):
    """
    Insert 80 after index 90 in the given list and return the result.
    """
    return lst[:91] + [80] + lst[91:]