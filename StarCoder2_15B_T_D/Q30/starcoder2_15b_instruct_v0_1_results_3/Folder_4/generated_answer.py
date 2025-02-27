def insert_before_character(s):
    """
    Inserts character '6' before any occurrences of character 'a' in a string.
    """
    result = ''
    for c in s:
        result += c
        if c == 'a':
            result += '6'
    return result