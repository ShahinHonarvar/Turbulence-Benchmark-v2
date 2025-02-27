def return_n_smallest_chars(string):
    """
    Return a list of the 80 characters of the given string that have the smallest ASCII values.
    """
    sorted_chars = sorted(string)
    smallest_chars = sorted_chars[:80]
    return smallest_chars