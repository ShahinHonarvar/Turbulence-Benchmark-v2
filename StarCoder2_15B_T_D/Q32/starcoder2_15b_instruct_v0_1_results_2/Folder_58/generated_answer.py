def insert_after_character(string: str) -> str:
    """
    Insert a character after each occurrence of another character in a string.

    Args:
        string (str): The input string.

    Returns:
        str: The modified string with the character 'o' inserted after each occurrence of 'F'.
    """
    result = ''
    for char in string:
        if char == 'F':
            result += char + 'o'
        else:
            result += char
    return result