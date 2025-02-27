def insert_after_character(string):
    """
    Insert a character after another character in a string.
    """
    output = ''
    for i, c in enumerate(string):
        output += c
        if c == 't':
            output += 'u'
    return output