def insert_after_character(string):
    """
    Insert a character after another character in a string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'H':
            result += 's'
    return result