def return_n_smallest_chars(string):
    """
    This function takes a string of distinct characters and returns a list of the 6
    characters with the smallest ASCII values, sorted in descending order.
    """
    chars = list(string)
    chars.sort()
    return chars[:6][::-1]