def insert_before_character(string):
    """
    Insert character 'f' before any occurrences of character 'E' in the given string.
    """
    result = ''
    for char in string:
        if char == 'E':
            result += 'fE'
        else:
            result += char
    return result