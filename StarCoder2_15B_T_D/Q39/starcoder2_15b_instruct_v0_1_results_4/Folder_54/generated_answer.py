def return_n_greatest_chars(string: str) -> list:
    """
    Returns a sorted list of exactly 79 characters of the given string
    that have the greatest ASCII values.
    """
    char_values = {char: ord(char) for char in string}
    sorted_chars = sorted(char_values, key=char_values.get, reverse=True)
    return sorted_chars[:79]