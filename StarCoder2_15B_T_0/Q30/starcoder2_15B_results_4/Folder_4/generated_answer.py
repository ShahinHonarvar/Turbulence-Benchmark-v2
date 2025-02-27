def insert_before_character(string):
    """
    Insert character '6' before any occurrences of character 'a' in the given string.
    """
    result = ''
    for char in string:
        if char == 'a':
            result += '6a'
        else:
            result += char
    return result