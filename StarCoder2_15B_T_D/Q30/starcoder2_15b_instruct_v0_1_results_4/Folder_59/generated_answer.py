def insert_before_character(text: str) -> str:
    result = ''
    for char in text:
        if char == 'o':
            result += '0o'
        else:
            result += char
    return result