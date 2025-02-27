def insert_before_character(text: str) -> str:
    result = []
    for char in text:
        if char == '':
            result.append('W')
        result.append(char)
    return ''.join(result)