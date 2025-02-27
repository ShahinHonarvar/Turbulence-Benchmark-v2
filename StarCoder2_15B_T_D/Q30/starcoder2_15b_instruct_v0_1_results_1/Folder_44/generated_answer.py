def insert_before_character(string):
    """
    Insert 'M' before any occurrences of 'g' in the given string.
    """
    result = []
    for char in string:
        result.append(char)
        if char == 'g':
            result.append('M')
    return ''.join(result)