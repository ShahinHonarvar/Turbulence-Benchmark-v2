def insert_after_character(string):
    """
    Insert character '1' after every occurrence of character 'j' in a string.
    """
    new_string = ''
    for char in string:
        new_string += char
        if char == 'j':
            new_string += '1'
    return new_string