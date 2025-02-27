def insert_after_character(s: str) -> str:
    result = ''
    for c in s:
        result += c
        if c == 'i':
            result += '0'
    return result