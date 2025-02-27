def insert_before_character(string):
    """
    Insert 'P' before any occurrences of 'C' in a given string.
    """
    result = ''
    for char in string:
        if char == 'C':
            result += 'PC'
        else:
            result += char
    return result