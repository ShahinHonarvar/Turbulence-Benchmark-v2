def insert_before_character(string):
    """
    Insert character 'A' before any occurrences of character 'a' in a given string.
    """
    result = ''
    for character in string:
        if character == 'a':
            result += 'A'
        result += character
    return result