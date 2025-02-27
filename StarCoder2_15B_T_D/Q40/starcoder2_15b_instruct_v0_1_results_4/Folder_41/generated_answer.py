def return_n_smallest_chars(string):
    """
    Returns a list of the 37 smallest characters in'string'.
    """
    char_list = list(string)
    char_list.sort()
    return char_list[:37]