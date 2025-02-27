def insert_before_character(s: str) -> str:
    result = []
    for c in s:
        result.append(c)
        if c == '5':
            result.append('h')
    return ''.join(result)