def insert_before_character(s: str) -> str:
    result = ''
    for c in s:
        if c == '9':
            result += 'M9'
        else:
            result += c
    return result