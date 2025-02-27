def insert_before_character(s: str) -> str:
    result = []
    for i, c in enumerate(s):
        if c == 'a':
            result.append('t')
        result.append(c)
    return ''.join(result)