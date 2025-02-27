def insert_before_character(string: str) -> str:
    result = ''
    for i, c in enumerate(string):
        if c == 'a':
            result += 'W'
        result += c
    return result