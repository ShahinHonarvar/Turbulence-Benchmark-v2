def insert_after_character(string):
    """
    Insert character 'W' after every occurrence of character 'a' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'a':
            result += 'W'
    return result