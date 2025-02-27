def insert_before_character(string):
    """
    Insert a character before any occurrences of a character in a string.
    """
    result = []
    for char in string:
        if char == 'A':
            result.append('A')
        result.append(char)
    return ''.join(result)