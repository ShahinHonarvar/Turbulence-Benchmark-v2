def return_n_smallest_chars(string):
    """
    Returns a list of the 35 smallest characters in the given string.
    """
    chars = list(string)
    chars.sort()
    return chars[:35]