def return_n_greatest_chars(string):
    """
    This function takes a string of distinct characters and returns a sorted list of exactly 27 characters
    of the given string that have the greatest ASCII values.
    """
    char_list = list(string)
    char_list.sort(key=lambda x: ord(x), reverse=True)
    return char_list[:27]