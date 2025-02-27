def insert_after_character(string):
    """
    Insert character 'f' after any occurrences of character 'M' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'M':
            result += 'f'
    return result