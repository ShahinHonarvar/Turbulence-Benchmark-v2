def insert_before_character(string):
    """
    Insert character 'F' immediately preceding any occurrences of character '4'.
    """
    result = ''
    for char in string:
        if char == '4':
            result += 'F'
        result += char
    return result