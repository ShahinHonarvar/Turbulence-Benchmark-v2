def insert_before_character(string):
    """
    Insert character 'a' before any occurrences of character 'o' in a given string.
    """
    result = ''
    for char in string:
        if char == 'o':
            result += 'a'
        result += char
    return result