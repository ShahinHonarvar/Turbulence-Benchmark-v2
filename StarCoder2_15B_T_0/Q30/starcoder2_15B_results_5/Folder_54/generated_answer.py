def insert_before_character(string):
    """
    Insert character 'f' before any occurrences of character 'M' in a given string.
    """
    result = ''
    for char in string:
        if char == 'M':
            result += 'f'
        result += char
    return result