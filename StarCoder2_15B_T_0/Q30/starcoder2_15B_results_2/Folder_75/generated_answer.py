def insert_before_character(string):
    """
    Insert character 'q' before any occurrences of character 'U' in a given string.
    """
    result = ''
    for char in string:
        if char == 'U':
            result += 'qU'
        else:
            result += char
    return result