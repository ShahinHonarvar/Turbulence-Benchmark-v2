def insert_before_character(string):
    """
    Insert character 'v' before any occurrences of character 'j' in the given string.
    """
    result = ''
    for char in string:
        if char == 'j':
            result += 'vj'
        else:
            result += char
    return result