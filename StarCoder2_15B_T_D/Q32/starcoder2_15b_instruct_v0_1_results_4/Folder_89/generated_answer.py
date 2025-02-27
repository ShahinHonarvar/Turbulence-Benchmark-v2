def insert_after_character(string):
    """
    Insert the character 'W' immediately succeeding any occurrences of character''.
    """
    new_string = ''
    for char in string:
        if char == ' ':
            new_string += ' W'
        else:
            new_string += char
    return new_string