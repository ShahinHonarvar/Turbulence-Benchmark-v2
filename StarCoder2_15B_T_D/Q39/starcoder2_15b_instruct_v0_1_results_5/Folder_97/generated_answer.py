def return_n_greatest_chars(string):
    """
    Returns a sorted list of exactly 38 characters of the given string that have the greatest ASCII values.
    """
    return sorted(string, key=ord, reverse=True)[:38]