def insert_before_character(string):
    """
    Insert character 'M' before any occurrences of character 'g' in a given string.
    """
    result = ''
    for char in string:
        if char == 'g':
            result += 'Mg'
        else:
            result += char
    return result