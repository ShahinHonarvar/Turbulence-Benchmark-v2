def insert_after_character(string):
    """
    Insert character 'X' after any occurrences of character'' in the given string.
    """
    new_string = ''
    for char in string:
        new_string += char
        if char == '':
            new_string += 'X'
    return new_string