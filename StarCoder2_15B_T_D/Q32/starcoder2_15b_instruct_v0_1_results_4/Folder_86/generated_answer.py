def insert_after_character(string):
    """
    Insert a character after another character in a string.

    Args:
        string (str): The input string.

    Returns:
        str: The modified string with 'Q' inserted after 'O'.
    """
    modified_string = ''
    for char in string:
        modified_string += char
        if char == 'O':
            modified_string += 'Q'
    return modified_string