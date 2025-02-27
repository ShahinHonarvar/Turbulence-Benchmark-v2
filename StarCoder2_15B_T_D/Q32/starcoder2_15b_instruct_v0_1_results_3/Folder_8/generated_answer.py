def insert_after_character(string: str) -> str:
    result = []
    for char in string:
        result.append(char)
        if char == 'E':
            result.append('T')
    return ''.join(result)