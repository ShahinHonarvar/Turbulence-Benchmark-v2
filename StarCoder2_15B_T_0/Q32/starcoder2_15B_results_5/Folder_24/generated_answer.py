def insert_after_character(string):
    """
    Insert character '4' after any occurrences of character '0' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == '0':
            result += '4'
    return result