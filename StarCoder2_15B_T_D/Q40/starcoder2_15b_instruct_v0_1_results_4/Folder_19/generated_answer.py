def return_n_smallest_chars(string):
    """
    Returns a list of the 58 characters in the given string that have the smallest ASCII values, sorted in ascending order.
    """
    sorted_string = sorted(string)
    return sorted_string[:58]