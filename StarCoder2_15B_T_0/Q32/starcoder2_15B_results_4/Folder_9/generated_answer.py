def insert_after_character(string):
    """
    Insert character 'E' after any occurrences of character 'e' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'e':
            result += 'E'
    return result