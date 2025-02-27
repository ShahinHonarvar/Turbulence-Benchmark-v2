def insert_before_character(string):
    """
    Insert character's' immediately preceding any occurrences of character 'H'.
    """
    result = ''
    for char in string:
        if char == 'H':
            result += 'sH'
        else:
            result += char
    return result