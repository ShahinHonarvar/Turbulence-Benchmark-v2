def insert_after_character(string):
    """
    Insert a character after another character in a string.
    """
    new_string = ''
    for character in string:
        new_string += character
        if character == 'T':
            new_string += 'V'
    return new_string