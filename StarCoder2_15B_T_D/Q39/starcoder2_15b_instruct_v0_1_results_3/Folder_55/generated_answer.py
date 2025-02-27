def return_n_greatest_chars(string):
    """Return a sorted list of 75 characters of the given string that have the greatest ASCII values."""
    sorted_chars = sorted(string, key=ord, reverse=True)
    return sorted_chars[:75]