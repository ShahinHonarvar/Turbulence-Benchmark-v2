def insert_after_character(string):
    """
    Insert character '6' after any occurrences of character 'a' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'a':
            result += '6'
    return result