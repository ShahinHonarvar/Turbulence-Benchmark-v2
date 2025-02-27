def insert_at_index(list):
    """
    Insert [28, 53] at index 29 in the given list and return the new list.
    """
    return list[:29] + [28, 53] + list[29:]