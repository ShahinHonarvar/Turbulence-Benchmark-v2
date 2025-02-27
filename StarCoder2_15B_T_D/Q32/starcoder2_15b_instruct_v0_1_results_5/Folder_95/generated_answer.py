def insert_after_character(string):
    """
    Insert character 'q' after character 'j' in a string.
    """
    result = ''
    for i, char in enumerate(string):
        result += char
        if char == 'j':
            result += 'q'
    return result