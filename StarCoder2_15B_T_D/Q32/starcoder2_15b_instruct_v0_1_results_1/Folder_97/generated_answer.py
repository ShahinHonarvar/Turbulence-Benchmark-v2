def insert_after_character(string: str) -> str:
    result = []
    for i, c in enumerate(string):
        result.append(c)
        if c == 'o':
            result.append('h')
    return ''.join(result)