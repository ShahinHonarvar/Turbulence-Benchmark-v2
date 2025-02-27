def insert_after_character(string):
    """
    Insert character 'N' after any occurrences of character 'x' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'x':
            result += 'N'
    return result