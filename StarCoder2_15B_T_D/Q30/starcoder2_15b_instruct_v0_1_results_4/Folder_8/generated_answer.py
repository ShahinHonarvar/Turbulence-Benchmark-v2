def insert_before_character(string):
    """
    Insert character 'T' before any occurrences of 'E' in the input string.
    """
    new_string = ''
    for char in string:
        if char == 'E':
            new_string += 'TE'
        else:
            new_string += char
    return new_string