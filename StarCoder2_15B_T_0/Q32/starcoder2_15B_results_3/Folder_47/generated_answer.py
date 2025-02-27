def insert_after_character(string):
    """
    Insert character 'f' after any occurrences of character 'E' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'E':
            result += 'f'
    return result