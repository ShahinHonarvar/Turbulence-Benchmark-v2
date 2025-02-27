def insert_after_character(text):
    """
    Insert a character after another character in a string.
    """
    result = ''
    for char in text:
        result += char
        if char == 'A':
            result += 'a'
    return result