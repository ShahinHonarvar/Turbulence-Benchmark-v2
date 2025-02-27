def insert_before_character(text):
    """
    Insert character 'Q' immediately before any occurrences of character 'O'.
    """
    result = []
    for char in text:
        if char == 'O':
            result.append('Q')
        result.append(char)
    return ''.join(result)