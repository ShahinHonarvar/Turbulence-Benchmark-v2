def insert_before_character(string):
    """
    Insert character 'y' before any occurrences of character 'b' in a given string.
    """
    result = ''
    for char in string:
        if char == 'b':
            result += 'yb'
        else:
            result += char
    return result