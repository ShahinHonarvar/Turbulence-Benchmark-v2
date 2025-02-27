def insert_before_character(string):
    """
    Insert character 'M' before any occurrences of character 'g' in the given string.
    """
    new_string = ''
    for char in string:
        if char == 'g':
            new_string += 'Mg'
        else:
            new_string += char
    return new_string