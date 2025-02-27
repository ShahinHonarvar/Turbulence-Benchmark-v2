def insert_after_character(string: str) -> str:
    """
    Inserts character 'e' immediately succeeding any occurrences of character 'e'
    in the given string.
    """
    result = ''
    for char in string:
        result += char
        if char == 'e':
            result += 'e'
    return result