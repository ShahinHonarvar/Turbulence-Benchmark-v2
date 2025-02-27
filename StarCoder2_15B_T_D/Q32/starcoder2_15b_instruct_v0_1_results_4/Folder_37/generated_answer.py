def insert_after_character(string):
    """
    Insert character 'a' immediately succeeding any occurrences of character 'U'.
    """
    new_string = ''
    for char in string:
        new_string += char
        if char == 'U':
            new_string += 'a'
    return new_string