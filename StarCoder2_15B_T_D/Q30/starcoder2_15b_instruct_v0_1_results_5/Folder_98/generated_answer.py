def insert_before_character(s: str) -> str:
    result = ''
    for c in s:
        if c == 'U':
            result += 'uU'
        else:
            result += c
    return result