def insert_before_character(string):
    """
    Insert character 'w' before any occurrences of character 'r' in a given string.
    """
    result = ''
    for char in string:
        if char == 'r':
            result += 'wr'
        else:
            result += char
    return result