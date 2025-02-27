def insert_before_character(text):
    """
    Insert character 'G' immediately preceding any occurrences of character 't' in the given text.
    """
    result = ''
    for char in text:
        if char == 't':
            result += 'Gt'
        else:
            result += char
    return result