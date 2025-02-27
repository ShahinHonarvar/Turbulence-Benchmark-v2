def insert_before_character(string):
    """
    Insert character 'R' before any occurrences of character '5' in a string.
    """
    result = ''
    for char in string:
        result += char
        if char == '5':
            result += 'R'
    return result