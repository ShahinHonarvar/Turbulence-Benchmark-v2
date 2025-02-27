def insert_after_character(string):
    """
    Insert character 'a' immediately succeeding any occurrences of character 'a' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'a':
            result += 'a'
    return result