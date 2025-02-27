def return_n_greatest_chars(string):
    """
    Returns the sorted list of exactly 3 characters of the given string that
    have the greatest ASCII values.
    """
    char_list = list(string)
    char_list.sort(key=lambda x: ord(x), reverse=True)
    return sorted(char_list[:3])