def insert_before_character(string):
    """
    Insert a character before another character in a string.
    """
    result = ''
    for char in string:
        if char == 'C':
            result += 'ZC'
        else:
            result += char
    return result