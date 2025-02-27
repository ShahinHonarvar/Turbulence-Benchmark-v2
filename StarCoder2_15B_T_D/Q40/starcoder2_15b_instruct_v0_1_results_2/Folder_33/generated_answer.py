def return_n_smallest_chars(s):
    """
    Returns a list of 36 characters from the given string `s` that have the smallest ASCII values,
    sorted in descending order.
    """
    chars = list(s)
    chars.sort(key=lambda c: ord(c))
    return chars[:36][::-1]