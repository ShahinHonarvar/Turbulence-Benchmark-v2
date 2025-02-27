def insert_after_character(s: str) -> str:
    """
    Inserts character 'a' immediately succeeding any occurrences of character 'o' in a string.
    """
    result = []
    for c in s:
        result.append(c)
        if c == 'o':
            result.append('a')
    return ''.join(result)