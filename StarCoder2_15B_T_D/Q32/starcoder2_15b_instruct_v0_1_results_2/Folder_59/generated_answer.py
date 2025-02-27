def insert_after_character(text):
    """
    Insert a character after another character in a string.
    """
    new_text = ''
    for i, c in enumerate(text):
        new_text += c
        if c == 'o':
            new_text += '0'
    return new_text