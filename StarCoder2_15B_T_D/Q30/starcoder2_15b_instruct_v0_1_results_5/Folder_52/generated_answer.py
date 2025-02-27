def insert_before_character(string):
    """Insert a character before another character in a string."""
    result = ''
    for i, char in enumerate(string):
        if char == 'T':
            result += 'V'
        result += char
    return result