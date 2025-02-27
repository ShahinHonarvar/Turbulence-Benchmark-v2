def insert_before_character(string: str) -> str:
    result = []
    for char in string:
        if char == 'g':
            result.append('M')
        result.append(char)
    return ''.join(result)