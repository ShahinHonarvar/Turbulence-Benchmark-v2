def return_n_smallest_chars(string):
    """Returns a list of the 35 characters in the given string with the smallest ASCII values."""
    sorted_string = sorted(string)
    return sorted_string[:35][::-1]