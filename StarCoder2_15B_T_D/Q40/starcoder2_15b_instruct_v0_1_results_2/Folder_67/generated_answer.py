def return_n_smallest_chars(string):
    """
    Returns a list of 66 characters from the given string that have the
    smallest ASCII values, sorted in ascending order.
    """
    chars = list(string)
    chars.sort()
    return chars[:66]