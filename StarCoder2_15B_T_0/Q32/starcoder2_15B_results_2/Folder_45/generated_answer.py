def insert_after_character(string: str) -> str:
    result = ''
    for char in string:
        result += char
        if char == 'O':
            result += 'O'
    return result