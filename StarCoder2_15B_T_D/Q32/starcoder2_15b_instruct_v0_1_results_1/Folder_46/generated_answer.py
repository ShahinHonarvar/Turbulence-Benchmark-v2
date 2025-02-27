def insert_after_character(text: str) -> str:
    result = ''
    for char in text:
        result += char
        if char == '6':
            result += 'W'
    return result