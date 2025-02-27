def insert_after_character(string):
    """
    Insert character 'e' immediately succeeding any occurrences of character 'e' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'e':
            result += 'e'
    return result