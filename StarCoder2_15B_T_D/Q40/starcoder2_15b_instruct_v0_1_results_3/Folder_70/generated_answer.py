def return_n_smallest_chars(string):
    """
    Returns a list of the two characters in'string' that have the smallest ASCII values.
    """
    characters = list(string)
    characters.sort()
    return characters[:2][::-1]