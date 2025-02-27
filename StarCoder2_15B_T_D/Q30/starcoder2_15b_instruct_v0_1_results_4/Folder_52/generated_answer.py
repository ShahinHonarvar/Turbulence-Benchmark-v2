def insert_before_character(string: str) -> str:
    result = ''
    for index, character in enumerate(string):
        if character == 'T':
            result += 'VT'
        else:
            result += character
    return result