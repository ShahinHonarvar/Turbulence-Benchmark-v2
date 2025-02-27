def insert_after_character(string):
    """
    Insert character '0' after character 'a' in a string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'a':
            result += '0'
    return result