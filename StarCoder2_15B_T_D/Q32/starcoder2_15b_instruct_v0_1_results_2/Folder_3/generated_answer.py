def insert_after_character(string: str) -> str:
    result = ''
    for character in string:
        result += character
        if character == '0':
            result += 'H'
    return result