def return_n_greatest_chars(string):
    """
    Returns a sorted list of exactly 24 characters of the given string that have the greatest ASCII values.
    """
    characters = list(string)
    characters.sort(key=ord, reverse=True)
    return sorted(characters[:24])