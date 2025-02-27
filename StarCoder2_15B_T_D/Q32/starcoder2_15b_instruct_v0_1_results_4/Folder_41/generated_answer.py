def insert_after_character(s: str) -> str:
    """
    Inserts character 'o' immediately succeeding any occurrences of character 'O' in a string.
    """
    result = ''
    for c in s:
        result += c
        if c == 'O':
            result += 'o'
    return result