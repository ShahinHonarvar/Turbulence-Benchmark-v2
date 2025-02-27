def insert_after_character(string):
    """
    Insert a character after another character in a string.
    """
    new_string = ''
    for i, c in enumerate(string):
        if c == 'g':
            new_string += 'tg'
        else:
            new_string += c
    return new_string