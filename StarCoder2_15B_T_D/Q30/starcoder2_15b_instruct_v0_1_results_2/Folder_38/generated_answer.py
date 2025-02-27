def insert_before_character(s: str) -> str:
    result = ''
    for c in s:
        if c == 'X':
            result += '6X'
        else:
            result += c
    return result