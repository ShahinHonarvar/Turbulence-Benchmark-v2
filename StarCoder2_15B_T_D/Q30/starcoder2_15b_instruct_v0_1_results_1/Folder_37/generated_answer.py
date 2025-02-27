def insert_before_character(string: str) -> str:
    result = ''
    for i, c in enumerate(string):
        if c == 'U':
            result += 'a'
        result += c
    return result