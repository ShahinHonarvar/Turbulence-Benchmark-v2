def insert_before_character(string: str) -> str:
    result = []
    for char in string:
        if char == 'C':
            result.append('H')
        result.append(char)
    return ''.join(result)