def return_n_greatest_chars(s):
    """
    Returns a sorted list of exactly 84 characters of the given string `s` that have the greatest ASCII values.
    """
    sorted_chars = sorted(s, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:84]