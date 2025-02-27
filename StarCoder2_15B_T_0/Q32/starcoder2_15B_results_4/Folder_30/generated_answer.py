def insert_after_character(string: str) -> str:
    result = ''
    for char in string:
        result += char
        if char == '4':
            result += 'F'
    return result