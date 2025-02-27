def insert_before_character(string):
    """
    Insert character 'Z' immediately preceding any occurrences of character 'C'.
    """
    result = ''
    for char in string:
        result += char
        if char == 'C':
            result += 'Z'
    return result