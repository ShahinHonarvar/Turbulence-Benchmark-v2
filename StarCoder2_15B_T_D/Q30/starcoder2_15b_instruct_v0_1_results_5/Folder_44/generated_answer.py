def insert_before_character(s: str) -> str:
    result = ''
    for i, c in enumerate(s):
        if c == 'g':
            result += 'Mg'
        else:
            result += c
    return result