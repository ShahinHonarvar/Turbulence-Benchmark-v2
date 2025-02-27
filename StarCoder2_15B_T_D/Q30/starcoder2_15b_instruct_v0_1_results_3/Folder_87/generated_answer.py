def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'm':
            result += 'Nm'
        else:
            result += char
    return result