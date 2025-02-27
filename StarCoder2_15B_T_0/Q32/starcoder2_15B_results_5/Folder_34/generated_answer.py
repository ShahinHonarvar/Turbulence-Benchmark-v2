def insert_after_character(string):
    """
    Insert character 'a' after any occurrences of character 'A' in a string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'A':
            result += 'a'
    return result