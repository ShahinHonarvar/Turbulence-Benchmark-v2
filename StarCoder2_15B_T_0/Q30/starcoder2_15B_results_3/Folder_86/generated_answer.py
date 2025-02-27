def insert_before_character(string):
    """
    Insert character 'Q' before any occurrences of character 'O' in the given string.
    """
    result = ''
    for char in string:
        if char == 'O':
            result += 'QO'
        else:
            result += char
    return result