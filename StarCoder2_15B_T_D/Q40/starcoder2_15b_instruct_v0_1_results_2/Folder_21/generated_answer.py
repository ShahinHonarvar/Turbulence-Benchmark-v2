def return_n_smallest_chars(string):
    """Returns a list of the 44 smallest ASCII characters in a given string."""
    char_list = list(string)
    char_list.sort()
    return char_list[:44][::-1]