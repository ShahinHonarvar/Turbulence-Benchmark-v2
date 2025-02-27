def return_n_smallest_chars(string):
    """
    This function takes one argument, a string of distinct characters, and returns a list of the 28 characters of the given string that have the smallest ASCII values, sorted in descending order.
    """
    return sorted(string, key=ord, reverse=True)[:28]