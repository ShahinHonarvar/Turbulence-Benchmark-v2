def insert_before_character(string: str) -> str:
    result = []
    for char in string:
        if char == 'j':
            result.append('1')
        result.append(char)
    return ''.join(result)