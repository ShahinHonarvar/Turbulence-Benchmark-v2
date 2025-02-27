def return_n_smallest_chars(string):
    """
    Returns a list of 36 characters from the given string that have the smallest ASCII values.
    """
    char_list = list(string)
    char_list.sort()
    return char_list[:36]