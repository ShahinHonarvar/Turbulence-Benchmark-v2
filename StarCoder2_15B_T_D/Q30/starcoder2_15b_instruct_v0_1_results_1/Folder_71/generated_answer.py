def insert_before_character(string: str) -> str:
    result = []
    for char in string:
        if char == '2':
            result.append('S')
        result.append(char)
    return ''.join(result)