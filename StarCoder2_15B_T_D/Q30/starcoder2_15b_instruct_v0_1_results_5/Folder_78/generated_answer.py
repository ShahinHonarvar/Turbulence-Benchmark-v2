def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'H':
            result += 'sH'
        else:
            result += char
    return result