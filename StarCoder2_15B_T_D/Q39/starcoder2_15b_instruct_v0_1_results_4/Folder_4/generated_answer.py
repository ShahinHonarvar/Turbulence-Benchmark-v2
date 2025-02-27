def return_n_greatest_chars(string):
    """
    Returns a sorted list of exactly 90 characters of the given string that have the greatest ASCII values.
    """
    sorted_chars = sorted(string, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:90]