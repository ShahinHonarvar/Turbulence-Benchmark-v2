def insert_after_character(string):
    """
    Insert 'M' after any occurrences of '9' in the given string.
    """
    result = ''
    for char in string:
        result += char
        if char == '9':
            result += 'M'
    return result