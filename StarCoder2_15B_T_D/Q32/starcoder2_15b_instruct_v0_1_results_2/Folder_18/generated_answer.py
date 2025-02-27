def insert_after_character(string):
    """
    Insert character 'l' after any occurrences of character 'K' in the given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'K':
            result += 'l'
    return result