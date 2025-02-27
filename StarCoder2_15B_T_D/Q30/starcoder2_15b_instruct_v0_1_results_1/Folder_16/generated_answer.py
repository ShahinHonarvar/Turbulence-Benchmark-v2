def insert_before_character(s: str) -> str:
    result = []
    for c in s:
        result.append(c)
        if c == 'w':
            result.append('n')
    return ''.join(result)