def insert_after_character(string: str) -> str:
    result = []
    for char in string:
        result.append(char)
        if char == 'r':
            result.append('1')
    return ''.join(result)