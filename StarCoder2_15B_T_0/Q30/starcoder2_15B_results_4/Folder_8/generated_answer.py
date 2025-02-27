def insert_before_character(string):
    """
    Insert a character before another character in a string.
    """
    result = ''
    for i, c in enumerate(string):
        if c == 'E':
            result += 'TE'
        else:
            result += c
    return result