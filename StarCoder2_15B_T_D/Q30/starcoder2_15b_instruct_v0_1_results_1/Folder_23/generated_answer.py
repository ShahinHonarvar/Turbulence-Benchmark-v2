def insert_before_character(string: str) -> str:
    result = ''
    for i, c in enumerate(string):
        if c == 'b':
            result += 'y'
        result += c
    return result