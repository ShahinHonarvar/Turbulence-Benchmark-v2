def insert_before_character(string):
    """
    Insert the character 'W' immediately preceding any occurrences of the character '6' in a string.
    """
    new_string = ''
    for char in string:
        if char == '6':
            new_string += 'W6'
        else:
            new_string += char
    return new_string