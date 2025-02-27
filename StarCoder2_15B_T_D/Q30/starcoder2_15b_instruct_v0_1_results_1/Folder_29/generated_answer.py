def insert_before_character(string: str) -> str:
    result = ''
    for index, character in enumerate(string):
        if character == 'N':
            result += 'z'
        result += character
    return result