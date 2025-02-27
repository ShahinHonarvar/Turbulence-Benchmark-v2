def insert_after_character(string: str) -> str:
    result = ''
    for index, character in enumerate(string):
        result += character
        if character == 'b':
            result += 'y'
    return result