def insert_before_character(s: str) -> str:
    """
    Inserts character 'n' immediately preceding any occurrences of character 'H' in the given string.
    """
    result = ''
    for c in s:
        if c == 'H':
            result += 'n'
        result += c
    return result