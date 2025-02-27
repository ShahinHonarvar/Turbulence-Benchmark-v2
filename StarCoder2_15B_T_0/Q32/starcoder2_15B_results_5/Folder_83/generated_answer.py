def insert_after_character(string):
    """
    Insert character 'e' after any occurrences of character 'E' in a string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'E':
            result += 'e'
    return result