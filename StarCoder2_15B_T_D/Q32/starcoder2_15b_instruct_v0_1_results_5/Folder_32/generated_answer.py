def insert_after_character(string):
    """Insert 'u' after 'F' in a string."""
    result = ''
    for char in string:
        result += char
        if char == 'F':
            result += 'u'
    return result