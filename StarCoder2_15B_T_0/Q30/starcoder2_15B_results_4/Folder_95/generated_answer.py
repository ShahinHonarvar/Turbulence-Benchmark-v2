def insert_before_character(string):
    """
    Insert character 'q' before any occurrences of character 'j' in a given string.
    """
    result = ''
    for char in string:
        if char == 'j':
            result += 'qj'
        else:
            result += char
    return result