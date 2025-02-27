def insert_after_character(string):
    """
    Insert character 'I' after character 'Q' in a string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'Q':
            result += 'I'
    return result