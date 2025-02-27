def insert_before_character(string):
    """
    Insert the character 'o' immediately before any occurrences of the character 'F' in a string.
    """
    new_string = ''
    for char in string:
        if char == 'F':
            new_string += 'o'
        new_string += char
    return new_string