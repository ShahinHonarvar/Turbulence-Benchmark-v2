def insert_before_character(string):
    """
    Insert character 'o' before any occurrences of character 'F' in the given string.
    """
    result = ''
    for char in string:
        if char == 'F':
            result += 'oF'
        else:
            result += char
    return result