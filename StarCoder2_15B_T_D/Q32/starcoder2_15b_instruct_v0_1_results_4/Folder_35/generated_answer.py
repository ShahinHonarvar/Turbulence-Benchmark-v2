def insert_after_character(text):
    """
    Insert 'M' after every occurrence of '9' in the given text.
    """
    result = ''
    for char in text:
        result += char
        if char == '9':
            result += 'M'
    return result