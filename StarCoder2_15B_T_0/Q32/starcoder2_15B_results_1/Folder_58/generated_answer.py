def insert_after_character(string):
    """
    Insert character 'o' after any occurrences of character 'F' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'F':
            result += 'o'
    return result