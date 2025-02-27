def return_n_greatest_chars(string):
    """Return the first 68 characters of the given string sorted in ascending order based on their ASCII values."""
    chars = list(string)
    sorted_chars = sorted(chars)
    return sorted_chars[:68]