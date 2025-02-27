def insert_before_character(string):
    """Returns a string that is identical except that character '1' has been inserted immediately preceding any occurrences of character 'r'."""
    new_string = ''
    for char in string:
        new_string += char
        if char == 'r':
            new_string += '1'
    return new_string