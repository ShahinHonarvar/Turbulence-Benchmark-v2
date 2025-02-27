def insert_after_character(text: str) -> str:
    result = []
    for char in text:
        result.append(char)
        if char == 'i':
            result.append('I')
    return ''.join(result)