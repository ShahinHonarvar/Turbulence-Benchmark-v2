def insert_after_character(string: str) -> str:
    result = ''
    for character in string:
        result += character
        if character == 'u':
            result += 'u'
    return result