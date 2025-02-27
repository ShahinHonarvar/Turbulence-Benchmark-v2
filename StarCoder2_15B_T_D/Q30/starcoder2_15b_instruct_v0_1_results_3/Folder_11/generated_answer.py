def insert_before_character(string: str) -> str:
    result = ''
    for i, c in enumerate(string):
        result += c
        if c == 'g':
            result += 't'
    return result