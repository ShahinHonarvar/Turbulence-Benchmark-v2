def insert_after_character(string: str) -> str:
    result = []
    for char in string:
        result.append(char)
        if char == 'e':
            result.append('W')
    return ''.join(result)