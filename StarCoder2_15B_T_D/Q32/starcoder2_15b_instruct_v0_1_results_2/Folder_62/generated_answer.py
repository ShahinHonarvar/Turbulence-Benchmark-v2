def insert_after_character(string: str) -> str:
    result = []
    for i, c in enumerate(string):
        result.append(c)
        if c == '':
            result.append('o')
    return ''.join(result)