def insert_before_character(string):
    """
    Insert character 'I' immediately preceding any occurrences of character 'I'.
    """
    result = ''
    for char in string:
        result += char
        if char == 'I':
            result += 'I'
    return result