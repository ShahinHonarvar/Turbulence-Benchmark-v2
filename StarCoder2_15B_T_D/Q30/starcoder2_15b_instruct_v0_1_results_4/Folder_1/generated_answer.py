def insert_before_character(string):
    """
    Insert a character before another character in a string.
    """
    new_string = ''
    for index, char in enumerate(string):
        if char == 'U':
            new_string += 'T'
        new_string += char
    return new_string