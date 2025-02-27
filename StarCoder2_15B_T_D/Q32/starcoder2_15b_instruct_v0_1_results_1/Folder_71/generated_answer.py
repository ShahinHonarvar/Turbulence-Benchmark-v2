def insert_after_character(string):
    """
    Insert character 'S' immediately succeeding any occurrences of character '2'.
    """
    result = ''
    for char in string:
        result += char
        if char == '2':
            result += 'S'
    return result