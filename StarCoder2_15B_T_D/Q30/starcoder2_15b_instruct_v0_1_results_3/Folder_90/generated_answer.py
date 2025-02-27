def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'U':
            result += 'FU'
        else:
            result += char
    return result