def insert_after_index(input_list):
    """
    Insert [27, 34] into the given list at the index immediately succeeding index 38.
    """
    return input_list[:39] + [27, 34] + input_list[39:]