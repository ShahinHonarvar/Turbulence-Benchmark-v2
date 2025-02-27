def insert_after_character(string: str) -> str:
    result = ''
    for i, c in enumerate(string):
        result += c
        if c == 'a':
            result += 'W'
    return result