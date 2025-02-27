def insert_before_character(string: str) -> str:
    result = ''
    for i, char in enumerate(string):
        if char == 'A':
            result += 'H'
        result += char
    return result