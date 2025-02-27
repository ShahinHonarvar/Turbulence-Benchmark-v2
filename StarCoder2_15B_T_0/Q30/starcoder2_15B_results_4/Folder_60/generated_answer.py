def insert_before_character(string):
    """
    Insert character 'P' before any occurrences of character 'C' in a given string.
    """
    result = ''
    for char in string:
        if char == 'C':
            result += 'PC'
        else:
            result += char
    return result