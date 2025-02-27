def insert_before_character(string: str) -> str:
    result = ''
    for i, char in enumerate(string):
        if char == 'I':
            result += 'I'
        result += char
    return result