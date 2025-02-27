def return_n_greatest_chars(s):
    """
    Returns a sorted list of exactly 63 characters of the given string `s` that have the greatest ASCII values.
    """
    return sorted(s, reverse=True)[:63]