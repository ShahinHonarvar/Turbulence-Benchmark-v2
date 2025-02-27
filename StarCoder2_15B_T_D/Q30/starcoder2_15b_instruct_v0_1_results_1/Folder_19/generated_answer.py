def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == '5':
            result += 'h5'
        else:
            result += char
    return result