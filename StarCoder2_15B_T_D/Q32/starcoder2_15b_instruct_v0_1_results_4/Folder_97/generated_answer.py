def insert_after_character(string):
    """
    Insert a character after another character in a string.
    """
    result = ''
    for index, character in enumerate(string):
        if character == 'o':
            result += 'oh'
        else:
            result += character
    return result