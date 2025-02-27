def return_n_smallest_chars(string):
    """
    Returns a list of the 23 smallest characters in the given string.
    """
    sorted_string = sorted(string)
    return sorted_string[:23][::-1]