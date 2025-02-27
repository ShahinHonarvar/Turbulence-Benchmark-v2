def insert_before_character(string):
    """
    Insert character 'j' before any occurrences of character 'O' in the given string.
    """
    result = ''
    for char in string:
        if char == 'O':
            result += 'jO'
        else:
            result += char
    return result