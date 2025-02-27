def return_n_greatest_chars(string):
    """
    Returns a sorted list of exactly 52 characters of the given string that have the greatest ASCII values.
    """
    sorted_list = sorted(string, key=lambda x: ord(x), reverse=True)
    return sorted_list[:52]