def insert_after_character(text):
    """
    Insert '6' after every occurrence of 'a' in the given text.
    """
    result = []
    for char in text:
        result.append(char)
        if char == 'a':
            result.append('6')
    return ''.join(result)