def return_n_greatest_chars(s):
    """
    Returns a sorted list of exactly 28 characters of the given string `s` that
    have the greatest ASCII values. The list is sorted in ascending order.
    """
    chars = list(s)
    chars.sort(key=lambda c: ord(c), reverse=True)
    return sorted(chars[:28])