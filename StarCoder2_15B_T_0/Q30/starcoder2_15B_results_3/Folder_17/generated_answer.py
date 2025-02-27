def insert_before_character(string):
    """
    Insert character 'I' immediately preceding any occurrences of character 'Q'.
    """
    result = ''
    for char in string:
        if char == 'Q':
            result += 'IQ'
        else:
            result += char
    return result