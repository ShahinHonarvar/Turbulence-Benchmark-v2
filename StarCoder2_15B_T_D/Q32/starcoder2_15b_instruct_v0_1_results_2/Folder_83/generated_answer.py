def insert_after_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'E':
            result += 'Ee'
        else:
            result += char
    return result