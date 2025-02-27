def insert_after_index(lst: list) -> list:
    """
    Inserts [1, 7] into a list after the index 7.
    """
    lst.insert(7 + 1, [1, 7])
    return lst