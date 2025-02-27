def insert_after_character(string):
    """
    Insert a character after another character in a string.
    """
    result = ''
    for i, c in enumerate(string):
        result += c
        if c == '9':
            result += 'h'
    return result