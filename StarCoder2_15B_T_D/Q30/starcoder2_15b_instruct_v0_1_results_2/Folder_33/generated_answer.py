def insert_before_character(s: str) -> str:
    result = []
    for c in s:
        if c == 'a':
            result.append('n')
        result.append(c)
    return ''.join(result)