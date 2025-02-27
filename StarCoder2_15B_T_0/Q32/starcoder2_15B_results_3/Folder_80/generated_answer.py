def insert_after_character(string):
    """
    Insert character 'X' after any occurrences of character'' in the given string.
    """
    result = ''
    for char in string:
        result += char
        if char == ' ':
            result += 'X'
    return result