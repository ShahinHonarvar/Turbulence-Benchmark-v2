def return_n_greatest_chars(string):
    """
    Returns a sorted list of exactly 23 characters of the given string that have the greatest ASCII values.
    """
    sorted_string = sorted(string, key=ord, reverse=True)
    return sorted_string[:23]