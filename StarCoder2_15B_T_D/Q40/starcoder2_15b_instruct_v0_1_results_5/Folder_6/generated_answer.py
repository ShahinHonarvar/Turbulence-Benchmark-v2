def return_n_smallest_chars(string):
    """Return a list of the 47 smallest ASCII characters from a given string."""
    return sorted(string, key=ord)[-47:]