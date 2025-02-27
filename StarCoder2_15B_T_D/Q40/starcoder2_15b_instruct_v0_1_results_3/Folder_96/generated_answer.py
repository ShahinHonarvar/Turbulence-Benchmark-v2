def return_n_smallest_chars(string):
    """
    Returns a list of the 20 characters in'string' that have the smallest ASCII values, sorted in descending order.
    """
    chars = sorted(string)
    return chars[:20][::-1]