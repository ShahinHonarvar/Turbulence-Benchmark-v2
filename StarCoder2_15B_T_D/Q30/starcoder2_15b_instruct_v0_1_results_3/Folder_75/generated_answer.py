def insert_before_character(string):
    """
    Insert the character 'q' immediately preceding any occurrences of 'U' in the given string.
    """
    output = ''
    for char in string:
        if char == 'U':
            output += 'qU'
        else:
            output += char
    return output