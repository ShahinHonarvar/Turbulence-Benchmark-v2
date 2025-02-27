def insert_before_character(string):
    """
    Insert a character before another character in a string.
    """
    result = ''
    for i, c in enumerate(string):
        if c == 'P':
            result += 'VP'
        else:
            result += c
    return result