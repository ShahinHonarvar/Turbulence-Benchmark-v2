def insert_at_index(lst):
    """
    Given a list, return a list that is identical except that [98, 22] has been inserted at index 24.
    """
    return lst[:24] + [98, 22] + lst[24:]