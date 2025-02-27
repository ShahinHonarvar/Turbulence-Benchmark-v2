def insert_before_character(text: str) -> str:
    """
    Insert a character before each occurrence of a character in a given string.
    """
    result = ''
    for char in text:
        result += char
        if char == 'k':
            result += 'k'
    return result