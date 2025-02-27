def return_n_greatest_chars(string):
    """
    Returns a sorted list of exactly 3 characters of the given string
    that have the greatest ASCII values.
    """
    chars = list(string)
    chars.sort(key=lambda c: ord(c), reverse=True)
    return chars[:3]