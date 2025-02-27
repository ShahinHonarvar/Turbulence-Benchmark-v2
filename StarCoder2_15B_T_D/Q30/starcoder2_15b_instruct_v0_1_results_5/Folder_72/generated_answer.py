def insert_before_character(string):
    """
    Insert character 'd' immediately preceding any occurrences of character 'O'.
    """
    new_string = ''
    for char in string:
        if char == 'O':
            new_string += 'dO'
        else:
            new_string += char
    return new_string