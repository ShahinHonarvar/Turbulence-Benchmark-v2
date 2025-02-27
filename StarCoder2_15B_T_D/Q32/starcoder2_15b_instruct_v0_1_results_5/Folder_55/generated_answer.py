def insert_after_character(string: str) -> str:
    result = []
    for char in string:
        result.append(char)
        if char == 'u':
            result.append('U')
    return ''.join(result)