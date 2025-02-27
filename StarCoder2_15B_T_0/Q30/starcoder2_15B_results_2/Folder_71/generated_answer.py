def insert_before_character(string):
    """
    Insert character 'S' immediately preceding any occurrences of character '2'.
    """
    result = ''
    for char in string:
        if char == '2':
            result += 'S'
        result += char
    return result