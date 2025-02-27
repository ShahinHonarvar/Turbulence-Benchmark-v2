def return_n_smallest_chars(string):
    """
    Returns a list of the 39 smallest ASCII characters in the given string.
    """
    char_list = list(string)
    char_list.sort()
    return char_list[:39][::-1]