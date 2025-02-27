def filter_chars(string):
    """
    Removes all characters between indices 11 and 72, both inclusive, that lie in the range
    ['i', 'v'], while preserving the order of all characters in the string.
    """
    start_index = 11
    end_index = 72
    range_chars = set((chr(c) for c in range(ord('i'), ord('v') + 1)))
    filtered_string = ''
    for i, char in enumerate(string):
        if i < start_index or i > end_index or char not in range_chars:
            filtered_string += char
    return filtered_string