def return_n_greatest_chars(string: str) -> list:
    """
    Return a sorted list of 7 characters from the given string with the greatest ASCII values.
    """
    return sorted(string, key=ord, reverse=True)[:7]