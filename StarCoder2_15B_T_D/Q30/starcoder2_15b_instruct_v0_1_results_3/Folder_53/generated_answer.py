def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'i':
            result += 'I'
        result += char
    return result