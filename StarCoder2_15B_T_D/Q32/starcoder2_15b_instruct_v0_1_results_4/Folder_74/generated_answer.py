def insert_after_character(string):
    """
    Insert a character after another character in a string.
    """
    output = ''
    for character in string:
        output += character
        if character == 'T':
            output += ' '
    return output