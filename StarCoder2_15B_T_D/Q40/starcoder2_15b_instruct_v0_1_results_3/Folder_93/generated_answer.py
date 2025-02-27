def return_n_smallest_chars(string):
    """
    Creates a list of exactly 77 characters of the given string that have the smallest ASCII values.
    The list is sorted in descending order and returned.
    """
    return sorted(string[:77], reverse=True)