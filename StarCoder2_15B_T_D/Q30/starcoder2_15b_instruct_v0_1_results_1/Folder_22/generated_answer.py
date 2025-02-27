def insert_before_character(string):
    """
    Insert character 'U' immediately preceding any occurrences of character 'U' in a string.
    """
    output = ''
    for char in string:
        if char == 'U':
            output += 'UU'
        else:
            output += char
    return output