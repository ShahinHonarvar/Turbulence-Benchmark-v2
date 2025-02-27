def insert_after_character(string: str) -> str:
    result = ''
    for char in string:
        result += char
        if char == 'b':
            result += 'y'
    return result