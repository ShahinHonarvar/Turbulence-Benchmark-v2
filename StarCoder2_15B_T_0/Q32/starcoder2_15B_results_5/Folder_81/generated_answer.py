def insert_after_character(string):
    """
    Insert character 'A' immediately succeeding any occurrences of character 'A' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'A':
            result += 'A'
    return result