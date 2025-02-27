def insert_before_character(string: str) -> str:
    result = ''
    for character in string:
        if character == 'T':
            result += ' '
        result += character
    return result