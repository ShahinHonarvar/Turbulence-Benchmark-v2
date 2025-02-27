def insert_after_character(string: str) -> str:
    result = []
    for char in string:
        result.append(char)
        if char == 'o':
            result.append('0')
    return ''.join(result)