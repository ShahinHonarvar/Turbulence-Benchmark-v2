def insert_before_character(string):
    """
    Insert character 'q' immediately preceding any occurrences of character 'U'.
    """
    new_string = ''
    for i, c in enumerate(string):
        if c == 'U':
            new_string += 'q'
        new_string += c
    return new_string