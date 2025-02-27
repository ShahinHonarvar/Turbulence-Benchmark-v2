def insert_after_character(string):
    """
    Insert character 'A' after any occurrence of character 'a' in the given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'a':
            result += 'A'
    return result