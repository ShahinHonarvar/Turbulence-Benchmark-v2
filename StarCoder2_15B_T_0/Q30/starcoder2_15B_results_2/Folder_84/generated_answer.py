def insert_before_character(string):
    """
    Insert character 'n' immediately preceding any occurrences of character 'H'.
    """
    result = ''
    for char in string:
        if char == 'H':
            result += 'nH'
        else:
            result += char
    return result