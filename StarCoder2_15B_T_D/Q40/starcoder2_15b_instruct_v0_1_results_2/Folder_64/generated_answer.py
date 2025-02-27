def return_n_smallest_chars(string):
    """Returns a list of the 39 smallest ASCII characters in a given string."""
    sorted_chars = sorted(string, key=ord)
    return sorted_chars[:39][::-1]