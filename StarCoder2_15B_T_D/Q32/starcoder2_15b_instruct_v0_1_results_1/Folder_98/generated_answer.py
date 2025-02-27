def insert_after_character(s):
    """
    Insert a character after another character in a string.
    """
    result = ''
    for c in s:
        result += c
        if c == 'U':
            result += 'u'
    return result