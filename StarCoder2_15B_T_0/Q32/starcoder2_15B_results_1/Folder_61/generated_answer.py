def insert_after_character(string):
    """
    Insert character '0' after any occurrences of character 'e' in the given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'e':
            result += '0'
    return result