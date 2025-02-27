def insert_before_character(s: str) -> str:
    result = ''
    for i, c in enumerate(s):
        if c == 'e':
            result += 'e'
        result += c
    return result