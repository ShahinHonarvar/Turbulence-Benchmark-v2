def insert_after_character(string: str) -> str:
    result = ''
    for character in string:
        if character == '0':
            result += '0H'
        else:
            result += character
    return result