def insert_before_character(string):
    """
    Insert 'U' before any occurrences of 'U' in the input string.
    """
    new_string = ''
    for char in string:
        if char == 'U':
            new_string += 'UU'
        else:
            new_string += char
    return new_string