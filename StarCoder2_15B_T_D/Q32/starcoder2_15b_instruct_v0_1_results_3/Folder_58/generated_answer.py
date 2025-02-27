def insert_after_character(string: str) -> str:
    result = ''
    for i, char in enumerate(string):
        if char == 'F':
            result += 'Fo'
        else:
            result += char
    return result