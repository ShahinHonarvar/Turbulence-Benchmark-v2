def insert_before_character(s: str) -> str:
    result = ''
    for i, c in enumerate(s):
        if c == '0':
            result += '40'
        else:
            result += c
    return result