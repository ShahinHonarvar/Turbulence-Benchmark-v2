def insert_before_character(string):
    """
    Insert character 'F' before any occurrences of character 'U' in the given string.
    """
    result = ''
    for char in string:
        if char == 'U':
            result += 'FU'
        else:
            result += char
    return result