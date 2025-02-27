def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'j':
            result += '1j'
        else:
            result += char
    return result