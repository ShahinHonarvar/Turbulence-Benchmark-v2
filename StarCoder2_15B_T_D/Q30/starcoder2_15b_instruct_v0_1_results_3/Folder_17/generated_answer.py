def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'Q':
            result += 'IQ'
        else:
            result += char
    return result