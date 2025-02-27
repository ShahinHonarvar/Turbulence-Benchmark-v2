def insert_after_character(s: str) -> str:
    result = ''
    for c in s:
        result += c
        if c == 'a':
            result += 'A'
    return result