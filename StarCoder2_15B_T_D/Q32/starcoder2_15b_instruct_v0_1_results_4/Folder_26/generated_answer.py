def insert_after_character(text):
    """
    Insert a character after another character in a string.
    """
    output = ''
    for i, c in enumerate(text):
        output += c
        if c == 'r':
            output += 'w'
    return output