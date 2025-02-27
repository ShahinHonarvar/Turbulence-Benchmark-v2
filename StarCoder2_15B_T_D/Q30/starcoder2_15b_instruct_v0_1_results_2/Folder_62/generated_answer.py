def insert_before_character(string: str) -> str:
    result = ''
    for i, c in enumerate(string):
        if c == '':
            result += 'o'
        result += c
    return result