def insert_after_character(string: str) -> str:
    result = ''
    for char in string:
        if char == '0':
            result += ' 0'
        else:
            result += char
    return result