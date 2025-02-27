def insert_after_character(string: str) -> str:
    result = []
    for char in string:
        result.append(char)
        if char == 'A':
            result.append('a')
    return ''.join(result)