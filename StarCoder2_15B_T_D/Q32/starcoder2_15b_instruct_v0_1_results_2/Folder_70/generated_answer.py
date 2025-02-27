def insert_after_character(string: str) -> str:
    result = ''
    for index, character in enumerate(string):
        if character == 'P':
            result += 'PV'
        else:
            result += character
    return result