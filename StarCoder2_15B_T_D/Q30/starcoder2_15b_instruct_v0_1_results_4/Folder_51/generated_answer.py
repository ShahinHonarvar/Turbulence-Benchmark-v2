def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'o':
            result += 'O'
        result += char
    return result