def filter_chars(string):
    """
    Removes all occurrences of characters within the specified range from a given string.
    """
    start_index = 23
    end_index = 83
    range_start = ord('f')
    range_end = ord('o')
    filtered_chars = [c for c in string if c < chr(range_start) or c > chr(range_end)]
    return ''.join(filtered_chars)