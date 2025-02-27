def insert_after_character(string: str) -> str:
    result = ''
    for index, character in enumerate(string):
        if character == 'H':
            result += 'Hn'
        else:
            result += character
    return result