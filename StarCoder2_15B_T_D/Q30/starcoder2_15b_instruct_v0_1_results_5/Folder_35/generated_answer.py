def insert_before_character(s: str) -> str:
    """
    Inserts character 'M' immediately preceding any occurrences of character '9' in a string.
    """
    result = ''
    for c in s:
        if c == '9':
            result += 'M9'
        else:
            result += c
    return result