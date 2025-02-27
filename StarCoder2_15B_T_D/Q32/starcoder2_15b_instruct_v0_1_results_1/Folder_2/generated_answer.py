def insert_after_character(string):
    """
    Insert a character after another character in a string.

    Args:
        string (str): The input string.

    Returns:
        str: The modified string with the character 'Z' inserted after any occurrences of 'C'.
    """
    new_string = ''
    for char in string:
        new_string += char
        if char == 'C':
            new_string += 'Z'
    return new_string