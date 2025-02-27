def insert_after_character(string):
    """
    Insert character 'q' immediately succeeding any occurrences of character 'j'.
    """
    new_string = ''
    for char in string:
        new_string += char
        if char == 'j':
            new_string += 'q'
    return new_string