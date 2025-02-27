def insert_after_character(string: str) -> str:
    result = ''
    for i, char in enumerate(string):
        result += char
        if char == 'a':
            result += '6'
    return result