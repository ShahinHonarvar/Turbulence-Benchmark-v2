def insert_after_character(string):
    """
    Insert character 'y' after any occurrences of character 'b' in a string
    """
    result = ''
    for char in string:
        result += char
        if char == 'b':
            result += 'y'
    return result