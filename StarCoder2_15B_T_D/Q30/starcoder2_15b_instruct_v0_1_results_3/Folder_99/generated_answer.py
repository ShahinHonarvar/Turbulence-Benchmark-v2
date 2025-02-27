def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'a':
            result += 'W'
        result += char
    return result