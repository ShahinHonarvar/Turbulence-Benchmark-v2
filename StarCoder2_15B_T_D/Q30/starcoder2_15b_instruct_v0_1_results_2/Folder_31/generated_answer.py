def insert_before_character(string: str) -> str:
    result = ''
    for index, character in enumerate(string):
        if character == 'B':
            result += 'N'
        result += character
    return result