def insert_before_character(string: str) -> str:
    result = []
    for i, c in enumerate(string):
        if c == 'M':
            result.append('f')
        result.append(c)
    return ''.join(result)