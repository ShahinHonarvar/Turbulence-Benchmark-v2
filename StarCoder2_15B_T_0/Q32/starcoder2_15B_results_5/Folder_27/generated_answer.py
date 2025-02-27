def insert_after_character(string):
    """
    Insert character 'j' after any occurrences of character 'N' in a given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'N':
            result += 'j'
    return result