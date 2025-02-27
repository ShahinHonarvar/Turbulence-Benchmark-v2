def insert_before_character(string):
    """
    Insert character 'V' before character 'P'.
    """
    new_string = ''
    for i, c in enumerate(string):
        if c == 'P':
            new_string += 'V'
        new_string += c
    return new_string