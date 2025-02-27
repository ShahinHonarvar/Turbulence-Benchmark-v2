def return_n_smallest_chars(string):
    """Return a list of the 48 smallest ASCII characters in a given string."""
    chars = list(string)
    chars.sort()
    return chars[:48]