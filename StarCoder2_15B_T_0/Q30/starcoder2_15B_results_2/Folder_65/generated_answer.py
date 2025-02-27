def insert_before_character(string):
    """
    Insert character '9' before any occurrences of character '6' in a given string.
    """
    result = ''
    for char in string:
        if char == '6':
            result += '96'
        else:
            result += char
    return result