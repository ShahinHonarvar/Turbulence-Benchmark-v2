def insert_before_character(string: str) -> str:
    result = []
    for char in string:
        if char == '4':
            result.append('F')
        result.append(char)
    return ''.join(result)