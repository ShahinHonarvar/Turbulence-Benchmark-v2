def insert_before_character(string):
    """
    Insert character 'a' before any occurrences of character 'A' in a string.
    """
    result = ''
    for char in string:
        if char == 'A':
            result += 'aA'
        else:
            result += char
    return result