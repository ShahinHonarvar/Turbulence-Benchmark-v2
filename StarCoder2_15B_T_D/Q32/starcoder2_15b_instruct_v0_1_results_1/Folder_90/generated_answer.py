def insert_after_character(s):
    """
    Insert character 'F' after any occurrences of character 'U' in a string.
    """
    result = ''
    for c in s:
        result += c
        if c == 'U':
            result += 'F'
    return result