def insert_after_character(string):
    """
    Insert the character 'u' immediately succeeding any occurrences of character 'F' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'F':
            result += 'u'
    return result