def insert_after_character(string):
    """
    Insert character '1' after any occurrences of character 'j' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'j':
            result += '1'
    return result