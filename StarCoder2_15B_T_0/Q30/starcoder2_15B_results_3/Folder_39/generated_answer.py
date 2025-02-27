def insert_before_character(string):
    """
    Insert character 'Q' before any occurrences of character'm' in a given string.
    """
    result = ''
    for char in string:
        if char == 'm':
            result += 'Qm'
        else:
            result += char
    return result