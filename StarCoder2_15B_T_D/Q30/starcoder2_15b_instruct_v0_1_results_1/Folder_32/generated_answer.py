def insert_before_character(string):
    """
    Insert character 'u' immediately preceding any occurrences of character 'F' in a given string.
    """
    result = []
    for char in string:
        if char == 'F':
            result.append('u')
        result.append(char)
    return ''.join(result)