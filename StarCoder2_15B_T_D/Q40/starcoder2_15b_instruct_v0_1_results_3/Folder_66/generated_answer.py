def return_n_smallest_chars(string):
    """
    Returns a list of 33 characters from the given string that have the smallest ASCII values.
    """
    sorted_string = sorted(string)
    return sorted_string[:33][::-1]