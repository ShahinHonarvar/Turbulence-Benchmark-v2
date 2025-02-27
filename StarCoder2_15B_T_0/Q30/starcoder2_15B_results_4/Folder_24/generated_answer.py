def insert_before_character(string):
    """
    Insert character '4' before any occurrences of character '0' in the given string.
    """
    result = ''
    for char in string:
        if char == '0':
            result += '40'
        else:
            result += char
    return result