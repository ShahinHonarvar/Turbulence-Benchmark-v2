def insert_after_character(string):
    """
    Insert character '1' after any occurrences of character 'r' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'r':
            result += '1'
    return result