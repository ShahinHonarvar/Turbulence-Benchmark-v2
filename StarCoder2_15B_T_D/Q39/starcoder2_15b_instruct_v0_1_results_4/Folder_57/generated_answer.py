def return_n_greatest_chars(string):
    """
    Returns a sorted list of exactly 29 characters of the given string that have the greatest ASCII values.
    """
    char_list = list(string)
    char_list.sort(key=lambda x: ord(x), reverse=True)
    return char_list[:29]