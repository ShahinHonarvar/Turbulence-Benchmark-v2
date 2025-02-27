def insert_after_character(string):
    """
    Insert character 'E' immediately succeeding any occurrences of character 'E' in a given string.
    """
    result = ''
    for character in string:
        result += character
        if character == 'E':
            result += 'E'
    return result