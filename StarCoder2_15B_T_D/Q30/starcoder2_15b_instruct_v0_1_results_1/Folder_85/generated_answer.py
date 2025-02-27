def insert_before_character(string: str) -> str:
    result = []
    for char in string:
        if char == 'o':
            result.append('a')
        result.append(char)
    return ''.join(result)