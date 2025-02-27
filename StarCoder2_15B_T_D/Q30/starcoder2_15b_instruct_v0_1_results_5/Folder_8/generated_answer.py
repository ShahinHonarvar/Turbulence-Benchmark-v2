def insert_before_character(s: str) -> str:
    result = ''
    for c in s:
        if c == 'E':
            result += 'TE'
        else:
            result += c
    return result