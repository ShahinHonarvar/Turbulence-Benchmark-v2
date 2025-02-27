def insert_after_character(string):
    """
    Insert character 'M' after any occurrences of character 'g' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'g':
            result += 'M'
    return result